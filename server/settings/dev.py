from .base import *

ALLOWED_HOSTS = [".butter.local", ".ngrok.io"]
CORS_ORIGIN_REGEX_WHITELIST = (r"^(https?://)?(\w+\.)?butter\.local$",)
DEBUG = True
