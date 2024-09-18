import os
from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
MODEL_PATH  = os.environ.get('MODEL_PATH')