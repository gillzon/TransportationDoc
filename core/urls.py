
from django.urls import path, re_path

from rest_framework.routers import SimpleRouter
from core.viewsets.label import LabelViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v0.1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
app_name = 'core'
router = SimpleRouter()

router.register(r'label', LabelViewSet, basename="core")

urlpatterns = [
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
] + router.urls
