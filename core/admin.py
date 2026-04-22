from django.contrib import admin
from .models import Parceiro
from django.utils.html import format_html
from django.urls import reverse
from .models import Animal, AnimalFoto

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_atuacao', 'contato')
    search_fields = ('nome', 'area_atuacao')


class AnimalFotoInline(admin.TabularInline):
    model = AnimalFoto
    extra = 3

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    # O que aparece na tabela principal
    list_display = ('foto_miniatura', 'nome', 'especie', 'status', 'botao_apagar')
    list_filter = ('status', 'especie', 'sexo')
    search_fields = ('nome',)

    # O que aparece na tela de cadastro (em ordem vertical)
    fields = ('foto', 'nome', 'especie', 'sexo', 'idade', 'tamanho', 'status', 'historia')
    
    inlines = [AnimalFotoInline]

    def foto_miniatura(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;" />', obj.foto.url)
        return "Sem foto"
    
    def botao_apagar(self, obj):
        url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])
        return format_html('<a class="button" style="background-color: #dc3545; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none;" href="{}">Apagar</a>', url)