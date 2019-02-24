import requests
from .base import *

ALLOWED_HOSTS = [
    ".wilbur.app",
    # Plaid Webhook Hosts
    "52.21.26.131",
    "52.21.47.157",
    "52.41.247.19",
    "52.88.82.239",
]
CORS_ORIGIN_WHITELIST = ("api.wilbur.app", "wilbur.app")
DEBUG = True

EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get(
        "http://169.254.169.254/latest/meta-data/local-ipv4", timeout=0.01
    ).text
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
except requests.exceptions.RequestException:
    pass
