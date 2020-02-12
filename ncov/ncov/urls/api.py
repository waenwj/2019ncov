from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = "api"


schema_view = get_schema_view(
    openapi.Info(title="2019ncov API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    )
]


urlpatterns += [
    path("epidemic/", include("apps.epidemic.urls.api", namespace="epidemic")),
]
