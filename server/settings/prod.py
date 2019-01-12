from .base import *

ALLOWED_HOSTS = [
    ".wilbur.local",
    # Plaid Webhook Hosts
    "52.21.26.131",
    "52.21.47.157",
    "52.41.247.19",
    "52.88.82.239",
]
CORS_ORIGIN_WHITELIST = ("api.wilbur.app", "wilbur.app")
