from .base import *  # noqa
from .base import env

SECRET_KEY = env("SECRET_KEY", default="only dev replace me")

ALLOWED_HOSTS = ["*"]

# REST FRAMEWORK
# ----------------------------------------------------------------------------------------------------------------------
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "apps.ext.rest.pagination.PageNumberPagination",
    "PAGE_SIZE": 34,
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
}

# django extensions shell plus
# ----------------------------------------------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/shell_plus.html
SHELL_PLUS = "ptpython"
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000

SERV_TOKEN = env("SERV_TOKEN", default="")
POST_HEADERS = {
    "Authorization": f"edittoken {SERV_TOKEN}",
    "Content-Type": "application/json; charset=utf-8"
}
POST_URL = env("POST_URL", default=None)
POST_TOTAL_EPIDEMIC_URL = env("POST_TOTAL_EPIDEMIC_URL", default=None)


