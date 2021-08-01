from django.core.checks.security.base import SECRET_KEY_INSECURE_PREFIX
from django.core.management import utils

secret_key = SECRET_KEY_INSECURE_PREFIX + utils.get_random_secret_key()

print(f"SECRET_KEY = '{secret_key}'")
