import os

import environ

# access to Telegram login from code https://my.telegram.org/auth
# i get two things that are important — это api_id и api_hash

env = environ.Env()
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

api_id = env("API_ID")
api_hash = env("API_HASH")
