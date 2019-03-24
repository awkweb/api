from .base import *

ALLOWED_HOSTS = ["127.0.0.1", ".butter.local", ".ngrok.io"]
CORS_ORIGIN_REGEX_WHITELIST = (r"^(https?://)?(\w+\.)?butter\.local$",)
DEBUG = True
