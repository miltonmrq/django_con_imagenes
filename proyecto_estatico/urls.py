from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


