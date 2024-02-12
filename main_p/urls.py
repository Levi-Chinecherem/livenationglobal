# main_p/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="LiveNationGlobal API",
        default_version='v1',
        description="API documentation for LiveNationGlobal",
        terms_of_service="https://www.livenationglobal.com/terms-of-service",
        contact=openapi.Contact(email="contact@livenationglobal.com"),
        license=openapi.License(name="LiveNationGlobal License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/band/', include('band.urls')),
    path('api/chat/', include('chat.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

