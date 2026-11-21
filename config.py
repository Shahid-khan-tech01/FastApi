import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
     Secret_key = os.getenv("SECRET_KEY")
     Algorithm = os.getenv("ALGORITHM")

settings = Settings()