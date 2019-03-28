import os
from .base import *

ALLOWED_CIDR_NETS = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
ALLOWED_HOSTS = [
    ".butter.so",
    # Plaid Webhook Hosts
    "52.21.26.131",
    "52.21.47.157",
    "52.41.247.19",
    "52.88.82.239",
]
CORS_ORIGIN_REGEX_WHITELIST = (r"^(https?://)?(\w+\.)?butter\.so$",)
DEBUG = False
STATIC_URL = os.getenv("DJANGO_STATIC_URL")
