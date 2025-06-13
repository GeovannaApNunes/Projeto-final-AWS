# 🧭 Trilha AWS Ways – Uma Jornada de Estudos

**Protótipo de plataforma de estudos para a certificação AWS Cloud Practitioner**, desenvolvido como projeto final na [Escola da Nuvem](https://www.escoladanuvem.org/).

O objetivo é ajudar estudantes a se organizarem, acompanharem o progresso e manterem o foco nos estudos com recursos interativos e uma arquitetura moderna e escalável.

---

## 📌 Funcionalidades

- ✅ Registro de metas de estudo  
- 📑 Divisão de temas em subtemas  
- ✔️ Checklist interativo  
- 📊 Visualização de progresso (gráficos ou porcentagens)  
- 🔗 Adição de links e materiais extras  
- 🧠 Flashcards e vídeos educativos  
- 🤖 IA para recomendar trilhas personalizadas (Amazon Personalize)  
- 💬 Fórum para dúvidas e trocas entre estudantes

---

## ⚙️ Tecnologias e Serviços Utilizados

A plataforma foi construída com foco em escalabilidade, segurança e desempenho, utilizando os seguintes serviços AWS:

| Serviço                | Finalidade                              |
|------------------------|----------------------------------------|
| **Amazon S3**          | Hospedagem do front-end estático       |
| **Amazon CloudFront**  | Distribuição global de conteúdo        |
| **Amazon RDS**         | Banco de dados relacional              |
| **Amazon Cognito**     | Autenticação de usuários               |
| **Amazon API Gateway** | Gerenciamento das APIs                 |
| **AWS Lambda**         | Execução da lógica back-end (serverless) |
| **Amazon CloudWatch**  | Monitoramento e logs                   |
| **Amazon Route 53**    | Gerenciamento de DNS                   |
| **Amazon Personalize** | Recomendação de trilhas personalizadas |
| **Bedrock**            | Personalização de IA generativa        |

---

## 🖼️ Arquitetura da Aplicação

> A arquitetura segue um modelo **serverless**, focado em desempenho, escalabilidade e baixo custo.


![ways-01](https://github.com/user-attachments/assets/2daa3c26-7d18-4de6-8f6c-890b3bf2fefd)

---

### 🧩 Componentes e Fluxo

1. **Usuário** acessa a plataforma pelo navegador.
2. O **Front-end** (interface do usuário) estático é hospedado no **Amazon S3** e distribuído com **Amazon CloudFront**, garantindo acesso rápido e global.
3. As interações são enviadas para o **Amazon API Gateway**, que direciona as requisições para funções no **AWS Lambda**.
4. O **Lambda** executa a lógica da aplicação e se conecta ao **Amazon RDS**, onde os dados da plataforma são armazenados.
5. O **Amazon Cognito** é responsável por autenticar os usuários e gerenciar permissões de forma segura.
6. Para personalização da jornada de estudos, usamos:
   - **Amazon Personalize**, que recomenda trilhas de estudo com base no comportamento do usuário;
   - **Amazon Bedrock**, que fornece IA generativa para sugestões e interações inteligentes.
7. Toda a aplicação é monitorada com **Amazon CloudWatch**, que gera logs e alertas.
8. O **Amazon Route 53** gerencia o domínio e garante alta disponibilidade e roteamento eficiente.

---

## 🎯 Público-Alvo

- Estudantes se preparando para certificações AWS  
- Mentores e professores que desejam acompanhar o progresso de seus alunos  
- Comunidade de tecnologia e entusiastas de computação em nuvem  

---

## 👩‍💻 Equipe

Projeto desenvolvido por:

- **Geovanna Nunes** – [LinkedIn](https://www.linkedin.com/in/geovanna-nunes)  
- **Andrei Pereira** - [LinkedIn](https://www.linkedin.com/in/andrei-pereira)  
- **Iolanda Barreto** - [LinkedIn](https://www.linkedin.com/in/iolanda-barreto)  
- **Kamilly da Costa** - [LinkedIn](https://www.linkedin.com/in/kamillysilvadacosta)  
- **Rafael Bernasrdes** - [LinkedIn](https://www.linkedin.com/in/rafaelbernardesskz)  
- **João Lucas** - [LinkedIn](https://www.linkedin.com/in/joão-lucasslv)  


👩‍🏫 Orientação: [Professor Ricardo](https://linkedin.com/in/ricardosiminesscopim)

---

## 📚 Créditos

Projeto desenvolvido como parte da formação na [Escola da Nuvem](https://www.escoladanuvem.org/), com foco em capacitação e empregabilidade na área de computação em nuvem.

---

## ✨ Status

📌 Protótipo funcional – em fase de aprimoramentos e validação de ideias com usuários.
