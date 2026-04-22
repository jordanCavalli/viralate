from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('adotar/', views.adotar, name='adotar'),
    path('voluntariar/', views.voluntariar, name='voluntariar'),
    path('lares-temporarios/', views.lares_temporarios, name='lares_temporarios'),
    path('doar/', views.doar, name='doar'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('contato/', views.contato, name='contato'),
    path('enciclopet/', views.lista_enciclopet, name='enciclopet'),
    path('animal/<int:id>/', views.detalhes_animal, name='detalhes_animal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)