from dotenv import load_dotenv #Carrega as variáveis de ambiente
import os

load_dotenv()
api_key = os.getenv("HUGGING_FACE_API_TOKEN")

