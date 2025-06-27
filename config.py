import os
from datetime import timedelta
from dotenv import load_dotenv
import cloudinary.api

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    PORT = int(os.getenv("PORT"))
    SECRET_KEY = os.getenv("SECRET_KEY")
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "mkv"}
