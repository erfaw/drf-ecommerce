from .base import *
import os
from dotenv import load_dotenv
load_dotenv()

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('PRODUCTION_SECRET_KEY')
