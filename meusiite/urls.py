from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, produto_detail, buscar_produtos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # A URL aceita um número inteiro <int:id>
    path('produto/<int:id>/', produto_detail, name='produto_detail'),
    path('buscar_produtos/', buscar_produtos, name='buscar_produtos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

