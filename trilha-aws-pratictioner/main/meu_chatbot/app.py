from flask import Flask, render_template, request, jsonify
import unicodedata  # Para normalização de texto (remover acentos)
import re           # Para expressões regulares (limpar texto)
import html         # Para decodificar entidades HTML

app = Flask(__name__)

# --- Funções de Normalização e IA ---

def normalizar_texto(texto):
    """
    Normaliza o texto: minúsculas, remove acentos e pontuação, limpa espaços.
    Adicionado: Remoção de caracteres de controle e alguns símbolos problemáticos.
    """
    texto = texto.lower()
    # Remove acentos
    texto = unicodedata.normalize('NFKD', unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8'))
    
    # REMOÇÃO DE CARACTERES NÃO DESEJADOS:
    # Mantém letras (a-z), números (0-9), espaços, e hífens.
    # Qualquer outra coisa (pontuação, símbolos estranhos, caracteres de controle) é removida.
    texto = re.sub(r'[^a-z0-9\s-]', '', texto) 
    
    # Remove espaços múltiplos
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto


def ia_wayzi_sem_boto3(pergunta_usuario):
    """
    Processa a pergunta do usuário usando a lógica da Wayzi, sem interação com Boto3.
    """
    pergunta_normalizada = normalizar_texto(pergunta_usuario)

    # --- Respostas Estáticas ---
    respostas_estaticas = {
        # Cumprimentos
        ("ola", "oi", "ola wayzi", "oi wayzi"):
            "Olá! Sou a Wayzi, especialista em AWS Cloud Practitioner. Como posso ajudar você hoje?",

        # Identidade
        ("quem é você?", "quem e voce", "você e", "o que e voce"):
            "Sou uma assistente virtual especializada em computação em nuvem e AWS Cloud Practitioner!",

        # Conceitos AWS Gerais
        ("o que e aws", "fala sobre aws", "aws o que e"):
            "AWS é a Amazon Web Services, uma plataforma de computação em nuvem que oferece diversos serviços como computação, armazenamento, banco de dados e muito mais.",

        ("o que e ec2", "ec2", "elastic compute cloud", "instancia ec2"):
            "EC2 significa Elastic Compute Cloud, um serviço que permite criar e gerenciar servidores virtuais chamados instâncias. É como ter um computador na nuvem!",

        ("o que e s3", "s3", "simple storage service", "armazenamento s3", "bucket s3"):
            "S3 significa Simple Storage Service. É o serviço da AWS para armazenar objetos e arquivos de forma segura, escalável e altamente disponível, ideal para qualquer tipo de dado.",

        ("o que e rds", "rds", "relational database service", "banco de dados rds"):
            "RDS é o Relational Database Service da AWS. Ele facilita a configuração, operação e escalabilidade de bancos de dados relacionais (como MySQL, PostgreSQL, etc.) na nuvem.",

        ("o que e vpc", "vpc", "virtual private cloud", "rede vpc"):
            "VPC significa Virtual Private Cloud. É uma rede virtual dedicada e isolada dentro da AWS, onde você pode lançar seus recursos em uma rede isolada.",

        ("o que e iam", "iam", "identity and access management", "gerenciar usuarios aws"):
            "IAM significa Identity and Access Management. É o serviço da AWS para gerenciar usuários, grupos, permissões e políticas de segurança, controlando quem pode acessar o quê.",

        ("o que e lambda", "lambda", "aws lambda", "serverless lambda", "funcao lambda"):
            "AWS Lambda é um serviço de computação sem servidor que permite executar seu código em resposta a eventos sem precisar provisionar ou gerenciar servidores.",

        ("o que e dynamodb", "dynamodb", "aws dynamodb", "nosql dynamodb"):
            "DynamoDB é um serviço de banco de dados NoSQL totalmente gerenciado pela AWS, ideal para aplicações com alta performance, escalabilidade e baixa latência.",

        ("o que e cloudfront", "cloudfront", "aws cloudfront", "cdn cloudfront"):
            "CloudFront é um serviço de rede de entrega de conteúdo (CDN) da AWS que acelera a entrega de seu conteúdo web (imagens, vídeos, etc.) aos usuários finais globalmente.",

        # Casos de uso e comparações
        ("para que serve ec2", "quando usar ec2"):
            "O EC2 serve para hospedar aplicações, sites, servidores de banco de dados, servidores de jogos e muito mais, oferecendo controle total sobre o ambiente de computação.",

        ("qual a diferenca entre ec2 e lambda", "diferenca ec2 lambda"):
            "A principal diferença é que EC2 oferece servidores virtuais com controle total (você gerencia o S.O.), enquanto Lambda é serverless, executando seu código em resposta a eventos sem que você se preocupe com a infraestrutura de servidores.",
        
        # Otimização de Custos: EC2 Spot Instances
        ("o que e spot instance", "spot instance ec2", "instancia spot"):
            "Spot Instances são instâncias EC2 que permitem usar a capacidade EC2 ociosa a um custo muito reduzido. É ideal para cargas de trabalho flexíveis e que podem ser interrompidas.",

        # Confiabilidade: Regions e Availability Zones
        ("o que e regiao aws", "aws regions", "zona de disponibilidade", "availability zone"):
            "Uma Região AWS é uma área geográfica física isolada com várias Zonas de Disponibilidade. Uma Zona de Disponibilidade (AZ) é um ou mais data centers distintos dentro de uma Região, projetados para serem isolados de falhas de outras AZs.",

        # --- TRILHAS DE ESTUDO POR NÍVEL ---

        # Pergunta inicial sobre trilhas de estudo
        ("trilha de estudo", "como aprender aws", "caminho de aprendizado aws", "por onde comecar na aws"):
            "Para te ajudar melhor, qual o seu nível de conhecimento em AWS? Iniciante, intermediário ou você já tem alguma experiência?",

        # Respostas para cada nível e suas trilhas
        ("sou iniciante", "nivel iniciante", "estou comecando", "nao sei nada de aws", "iniciante"):
            "Ótimo! Para iniciantes em AWS, sugiro começar pelos **fundamentos da nuvem** e os serviços básicos. Você pode explorar: "
            "1. **Conceitos de Nuvem** "
            "2. **Modelo de Responsabilidade Compartilhada** "
            "3. **Serviços Essenciais** (EC2, S3, VPC, IAM) "
            "4. A **Certificação AWS Cloud Practitioner**. "
            "Qual desses tópicos você gostaria de entender primeiro? Diga, por exemplo, 'Conceitos de Nuvem' ou 'Fale sobre EC2'.",
        
        ("sou intermediario", "nivel intermediario", "ja tenho alguma experiencia aws", "intermediario"):
            "Excelente! Para usuários intermediários, podemos aprofundar em otimização, automação e arquiteturas mais complexas. Considere focar em:"
            "1. **Automação e Infraestrutura como Código** (CloudFormation, AWS CDK). "
            "2. **Serviços Serverless** (Lambda, DynamoDB, API Gateway). "
            "3. **Containers** (Amazon ECS, EKS). "
            "4. **Bancos de Dados Específicos** (RDS aprofundado, Aurora, DynamoDB). "
            "5. **Monitoramento e Logs** (CloudWatch, CloudTrail). "
            "6. **Otimização de Custos** (Cost Explorer, Savings Plans, Reserved Instances). "
            "Qual desses tópicos você gostaria de explorar mais a fundo?",
        
        ("sou avancado", "nivel avancado", "muita experiencia aws", "avançado", "experiente", "ja tenho experiencia aws", "nivel experiente"):
            "Impressionante! Para usuários avançados/experientes, o foco é em otimização de performance, segurança robusta, arquiteturas escaláveis e Machine Learning/Data Science na AWS. Que tal:"
            "1. **Machine Learning** (SageMaker, Rekognition). "
            "2. **Data Analytics:** Amazon Redshift, Athena, Kinesis."
            "3. **Segurança Avançada:** AWS Organizations (SCPs), Security Hub, WAF, Shield."
            "4. **Redes Avançadas:** Direct Connect, Transit Gateway."
            "5. **DevOps e CI/CD:** CodePipeline, CodeBuild, CodeDeploy."
            "6. **Otimização de Performance em Escala:** Estratégias para grandes workloads."
            "Qual área você gostaria de aprofundar para continuar expandindo seu conhecimento?",

        # --- APROFUNDAMENTOS PARA INICIANTES ---
        ("o que e cloud computing", "cloud computing", "computacao em nuvem", "o que e nuvem", "fale sobre conceitos de nuvem"):
            "**Cloud Computing** é a entrega de recursos de computação sob demanda, como servidores, armazenamento, bancos de dados, redes e software, pela internet, com um modelo de pagamento conforme o uso. Em vez de comprar, possuir e manter seus próprios data centers e servidores, você pode acessar esses recursos de um provedor de nuvem como a AWS. Pense nisso como alugar eletricidade em vez de ter sua própria usina!",
        
        ("quais os tipos de nuvem", "tipos de nuvem", "nuvem publica", "nuvem privada", "nuvem hibrida"):
            "Existem três modelos principais de implantação de nuvem: "
            "1. **Nuvem Pública:** Serviços de computação e armazenamento são oferecidos por provedores de terceiros (como a AWS) pela internet, disponíveis para o público em general. "
            "2. **Nuvem Privada:** Recursos de computação são exclusivos para uma única organização. Podem estar localizados no seu próprio data center ou ser gerenciados por um terceiro. "
            "3. **Nuvem Híbrida:** Uma combinação de nuvem pública e privada, permitindo que os dados e aplicativos se movam entre elas. É ótimo para flexibilidade e para manter dados sensíveis on-premise.",

        ("o que e iaas paas saas", "modelos de servico na nuvem", "iaas", "paas", "saas"):
            "Os modelos de serviço na nuvem definem o nível de gerenciamento que você tem sobre a infraestrutura: "
            "1. **IaaS (Infraestrutura como Serviço):** Você gerencia o sistema operacional, aplicações e dados, enquanto o provedor gerencia o hardware e virtualização. Ex: Amazon EC2. É como alugar o esqueleto de um prédio e mobiliá-lo. "
            "2. **PaaS (Plataforma como Serviço):** Você gerencia suas aplicações e dados, e o provedor gerencia o S.O., hardware e software da plataforma. Ex: AWS Elastic Beanstalk. É como alugar um apartamento mobiliado, você só se preocupa com suas coisas dentro dele. "
            "3. **SaaS (Software como Serviço):** Você apenas usa o software. O provedor gerencia toda a infraestrutura e aplicação. Ex: Gmail, Salesforce. É como pegar um táxi, você só informa o destino e usa o serviço.",

        ("o que e modelo de responsabilidade compartilhada aws", "modelo de responsabilidade compartilhada", "responsabilidade compartilhada aws"):
            "O **Modelo de Responsabilidade Compartilhada** da AWS é um framework de segurança crucial. Ele divide as responsabilidades de segurança entre a AWS e você, o cliente. "
            "**A AWS é responsável pela *segurança DA nuvem*** (Security *of* the Cloud) – isso inclui a infraestrutura física, hardware, software e rede que executa os serviços da AWS. "
            "**Você é responsável pela *segurança NA nuvem*** (Security *in* the Cloud) – isso abrange seus dados, configuração de segurança, gerenciamento do sistema operacional (se aplicável), configurações de rede (como Security Groups e ACLs de rede) e aplicações. É como um contrato de aluguel: a AWS constrói e mantém o prédio (a nuvem), e você é responsável por trancar a porta e o que você coloca dentro do seu apartamento (seus dados e configurações).",

        ("o que e servicos essenciais aws", "servicos essenciais iniciante"):
            "Os serviços essenciais para iniciar na AWS são: **EC2** (servidores virtuais), **S3** (armazenamento), **VPC** (sua rede na nuvem) e **IAM** (gerenciamento de usuários e permissões). Qual deles você gostaria de detalhar?",

        ("fale sobre ec2", "aprofundar ec2 iniciante"):
            "O **Amazon EC2 (Elastic Compute Cloud)** permite que você alugue servidores virtuais, chamados **instâncias**, na nuvem da AWS. Você pode escolher o sistema operacional, a quantidade de CPU e memória, e instalar o software que precisar. É ideal para rodar aplicações, sites e servidores que exigem controle total. Lembre-se que você gerencia o S.O. dentro da instância.",
        
        ("fale sobre s3", "aprofundar s3 iniciante"):
            "O **Amazon S3 (Simple Storage Service)** é um serviço de armazenamento de objetos altamente escalável, durável e disponível. Ele é ótimo para guardar qualquer tipo de arquivo (fotos, vídeos, backups), hospedar sites estáticos e como destino para logs de outros serviços. É um serviço serverless, ou seja, você não gerencia servidores.",

        ("o que e vpc detalhado", "aprofundar vpc iniciante", "vpc iniciante"):
            "A **Amazon VPC (Virtual Private Cloud)** permite que você lance recursos da AWS em uma rede virtual isolada, que é sua própria nuvem privada dentro da AWS. Você pode definir seus próprios endereços IP, sub-redes, tabelas de rotas e gateways de rede. É o que permite ter controle total sobre sua rede na nuvem, como se fosse seu próprio data center.",
        
        ("o que e iam detalhado", "aprofundar iam iniciante", "iam iniciante"):
            "O **AWS IAM (Identity and Access Management)** é o serviço para gerenciar o acesso de usuários, grupos e funções aos recursos da AWS. Com ele, você pode controlar **quem** pode acessar **o quê** e **quando** na sua conta AWS. É fundamental para a segurança, permitindo conceder apenas as permissões necessárias (princípio do menor privilégio).",

        ("o que e certificacao cloud practitioner", "certificacao aws iniciante", "prova cloud practitioner"):
            "A **Certificação AWS Cloud Practitioner** é um excelente ponto de partida para qualquer um que esteja começando na AWS. Ela valida um entendimento fundamental dos conceitos da nuvem AWS, serviços principais, segurança, arquitetura, preços e suporte. Não exige experiência técnica aprofundada, sendo ideal para quem busca uma base sólida ou para funções não técnicas.",

        # --- APROFUNDAMENTOS PARA INTERMEDIÁRIOS ---
        ("o que e cloudformation", "cloudformation", "infraestrutura como codigo cloudformation"):
            "**AWS CloudFormation** permite que você modele e provisione recursos da AWS de forma automatizada e repetível, usando arquivos de texto (templates JSON ou YAML). É como escrever a receita para sua infraestrutura, garantindo que ela seja sempre criada da mesma forma e facilitando a gestão de ambientes complexos. É um pilar da Infraestrutura como Código (IaC).",

        ("o que e aws cdk", "aws cdk", "cdk"):
            "O **AWS CDK (Cloud Development Kit)** é uma estrutura de desenvolvimento de software que permite definir seus recursos de nuvem usando linguagens de programação comuns (Python, TypeScript, Java, C#, Go). Ele 'compila' seu código para templates CloudFormation, oferecendo uma forma mais programática e menos verbosa de criar infraestrutura como código.",
        
        ("aprofundar lambda", "lambda intermediario", "lambda como funciona"):
            "O **AWS Lambda** é um serviço de computação *serverless* que executa seu código em resposta a eventos, sem que você precise provisionar ou gerenciar servidores. Você só paga pelo tempo de computação consumido. É ideal para tarefas sob demanda, processamento de dados e backends de aplicações web. Aprofundar em Lambda envolve entender triggers, ambientes de execução e o modelo de custo.",

        ("o que e api gateway", "api gateway aws"):
            "O **Amazon API Gateway** é um serviço gerenciado que facilita a criação, publicação, manutenção, monitoramento e segurança de APIs (Application Programming Interfaces) em qualquer escala. Ele atua como um 'front door' para suas aplicações, permitindo que você conecte, por exemplo, funções Lambda a endpoints HTTP acessíveis pela internet.",

        # --- NOVOS APROFUNDAMENTOS PARA AVANÇADOS ---
        ("machine learning aws", "sagemaker", "rekognition", "ml na aws", "aprofundar machine learning"):
            "Para **Machine Learning na AWS**, o **Amazon SageMaker** é uma plataforma abrangente que ajuda desenvolvedores e cientistas de dados a construir, treinar e implantar modelos de ML rapidamente. Já o **Amazon Rekognition** é um serviço de análise de imagem e vídeo que você pode usar para detectar objetos, pessoas, texto, cenas e atividades.",

        ("data analytics aws", "redshift", "athena", "kinesis", "aprofundar data analytics"):
            "Em **Data Analytics na AWS**, você pode usar o **Amazon Redshift** para um data warehouse escalável, o **Amazon Athena** para consultar dados em S3 usando SQL padrão, e o **Amazon Kinesis** para processamento de streaming de dados em tempo real.",

        ("seguranca avancada aws", "aws organizations", "security hub", "waf", "shield", "aprofundar seguranca"):
            "Para **Segurança Avançada na AWS**, o **AWS Organizations** ajuda a gerenciar e governar seus ambientes em escala com Controles de Serviço (SCPs). O **AWS Security Hub** fornece uma visão consolidada de seus alertas de segurança, e o **AWS WAF (Web Application Firewall)** e **AWS Shield** protegem suas aplicações web contra ataques e DDoS.",

        ("redes avancadas aws", "direct connect", "transit gateway", "aprofundar redes"):
            "Em **Redes Avançadas na AWS**, o **AWS Direct Connect** permite estabelecer uma conexão de rede privada e dedicada de sua on-premise para a AWS. O **AWS Transit Gateway** simplifica a conectividade entre VPCs e redes on-premise, agindo como um hub de rede centralizado.",

        ("devops aws", "ci cd aws", "codepipeline", "codebuild", "codedeploy", "aprofundar devops"):
            "Para **DevOps e CI/CD na AWS**, você tem serviços como **AWS CodePipeline** para automatizar seus pipelines de release, **AWS CodeBuild** para compilação de código e execução de testes, e **AWS CodeDeploy** para automatizar a implantação de aplicações em várias instâncias.",
        
        ("otimizacao de performance em escala", "performance em escala aws", "grandes workloads aws"):
            "A **Otimização de Performance em Escala** na AWS envolve diversas estratégias, como o uso de serviços gerenciados para escalabilidade automática (Auto Scaling Groups, SQS, DynamoDB), otimização de consultas de banco de dados, caching (ElastiCache), distribuição de carga (ELB) e monitoramento contínuo com CloudWatch para identificar gargalos.",

        # Despedidas
        ("obrigada, adeus", "tchau", "ate mais", "ate logo"):
            "Até mais! Qualquer dúvida sobre AWS ou computação em nuvem, estou à disposição!",
    }

    resposta_encontrada = None
    # Itera sobre as chaves (tuplas de palavras-chave) no dicionário
    for palavras_chave_tupla, resposta in respostas_estaticas.items():
        for palavra_chave in palavras_chave_tupla:
            # Verifica se a palavra-chave (normalizada) está contida na pergunta normalizada
            if palavra_chave in pergunta_normalizada:
                resposta_encontrada = resposta
                break # Encontrou uma correspondência, sai do loop interno
        if resposta_encontrada:
            break # Encontrou uma correspondência, sai do loop externo
    
    if resposta_encontrada:
        cleaned_response = html.unescape(resposta_encontrada)
        # Limpa qualquer caractere não-alfanumérico, exceto espaços e alguns símbolos desejados
        cleaned_response = re.sub(r'[^\w\s.,!?-]', '', cleaned_response) 
        return cleaned_response
    else:
        # Resposta padrão se nenhuma correspondência for encontrada
        return "Desculpe, não entendi. Pode reformular ou perguntar algo relacionado à AWS?"


# --- Rotas do Flask ---

@app.route('/')
def index():
    """Renderiza a página principal do chatbot."""
    return render_template('chatbot.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    """Recebe a pergunta do usuário e retorna a resposta da IA."""
    data = request.get_json()
    pergunta = data.get('pergunta', '')
    
    # Chama a função da IA sem Boto3
    resposta = ia_wayzi_sem_boto3(pergunta)
    
    print(f"Pergunta do Usuário: {pergunta}")
    print(f"Resposta da Wayzi: {resposta}")
    
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    print("Iniciando Wayzi... (Modo offline, sem conexão AWS)")
    app.run(debug=True)