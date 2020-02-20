from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("epidemic/", include("apps.epidemic.urls")),
]

#
# API
#
urlpatterns += [
    path("api/", include("ncov.urls.api", namespace="api")),
]
