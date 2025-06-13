import os
import boto3

def get_boto3_client(service_name, region_name='us-east-1', profile_name='seu-perfil-nome'):
    try:
        if profile_name:
            session = boto3.Session(profile_name=profile_name, region_name=region_name)
        else:
            session = boto3.Session(region_name=region_name)
        return session.client(service_name)
    except Exception as e:
        print(f"ERRO: {str(e)}")
        return None

def generate_chat_prompt(user_message, conversation_history=None, context=""):
    system_prompt = """
    Você é o Chatbot Ways, um assistente educacional especializado em AWS.
    Sua missão é ajudar alunos a estudar AWS, sugerindo trilhas personalizadas com base em suas dúvidas e progresso.
    """
    prompt = f"{system_prompt}\nUsuário: {user_message}\n"
    return prompt

def query_bedrock(message, model_params=None):
    client = get_boto3_client('bedrock-runtime')
    inference_profile_arn = "arn:aws:bedrock:us-east-1:YourAccountId:inference-profile/seu-modelo"
    
    if model_params is None:
        model_params = {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 250,
            "max_tokens": 1000,
            "response_format": {"type": "text"}
        }

    response = f"Simulação de resposta do Bedrock para: {message}"
    return response

def personalize_recommendations(user_id):
    return [f"Recomendação para usuário {user_id}: Curso AWS Básico", "Curso AWS Avançado"]
