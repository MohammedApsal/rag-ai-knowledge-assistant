import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME")
ENVIRONMENT = os.getenv("ENVIRONMENT")

print("Project:", PROJECT_NAME)
print("Environment:", ENVIRONMENT)