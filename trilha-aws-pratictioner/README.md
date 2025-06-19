# Chatbot Ways - Streamlit + AWS Bedrock

Este é o **Chatbot Ways**, um assistente educacional especializado em AWS, criado com **Streamlit** e preparado para integração com **Amazon Bedrock** e **Amazon Personalize**.

## 🚀 Funcionalidades

- ✅ Responde dúvidas sobre AWS com modelos do Amazon Bedrock.
- ✅ Gera trilhas de estudo personalizadas com Amazon Personalize (placeholder).
- ✅ Autenticação simples com usuário e senha.
- ✅ Código pronto para implantação local ou na AWS EC2.

---

## 📦 Como usar

### 1. Clonar o projeto e acessar a pasta:

```bash
unzip chatbot_ways_streamlit.zip
cd streamlit-base
```

### 2. Criar e ativar ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3. Instalar dependências:

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação:

```bash
cd streamlit
streamlit run app.py
```

Acesse no navegador: [http://localhost:8501](http://localhost:8501)

---

## 🔐 Acesso

- Usuário: **admin**
- Senha: **admin123**

Pode alterar em `app.py` → função `check_password()`.

---

## ⚙️ Configurações pendentes

1. Configurar perfil AWS em `.env`:  
```
AWS_PROFILE="seu-perfil-nome"
```

2. Ajustar o ARN do modelo Bedrock:  
Em `functions.py`:  
```
inference_profile_arn = "arn:aws:bedrock:us-east-1:YourAccountId:inference-profile/seu-modelo"
```

3. Integrar Amazon Personalize:  
Função `personalize_recommendations()` pronta para adaptação.

4. Substituir o ícone:  
Adicione `logo.jpeg` na pasta `streamlit/`.

---

## 📝 Contato

Desenvolvido por Geovanna Aparecida Nunes.  
Mentoria, dúvidas ou contribuições? Me procure!

