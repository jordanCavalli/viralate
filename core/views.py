from django.shortcuts import render, get_object_or_404
from .models import Parceiro
from .models import Animal


def home(request):
    return render(request, 'index.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')

def adotar(request):
    animais_destaque = Animal.objects.filter(status='ADOTAR').order_by('?')[:4]
    
    context = {
        'animais_destaque': animais_destaque
    }
    
    return render(request, 'adotar.html', context)

def voluntariar(request):
    return render(request, 'voluntariar.html')

def lares_temporarios(request):
    return render(request, 'lares_temporarios.html')

def doar(request):
    return render(request, 'doar.html')

def parceiros(request):
    parceiros_list = Parceiro.objects.all()
    return render(request, 'parceiros.html', {'parceiros': parceiros_list})

def contato(request):
    return render(request, 'contato.html')


def lista_enciclopet(request):
    # Traz todos os animais ordenados pelos mais recentes
    animais = Animal.objects.all().order_by('-data_cadastro')
    
    # Captura os filtros da URL
    busca = request.GET.get('busca')
    especie = request.GET.get('especie')
    sexo = request.GET.get('sexo')
    status = request.GET.get('status')
    tamanho = request.GET.get('tamanho')

    # Aplica os filtros apenas se o usuário tiver selecionado algo
    if busca:
        animais = animais.filter(nome__icontains=busca)
    if especie:
        animais = animais.filter(especie=especie)
    if sexo:
        animais = animais.filter(sexo=sexo)
    if status:
        animais = animais.filter(status=status)
    if tamanho:
        animais = animais.filter(tamanho=tamanho)

    context = {
        'animais': animais,
        'especies': Animal.ESPECIE_CHOICES,
        'sexos': Animal.SEXO_CHOICES,
        'status_choices': Animal.STATUS_CHOICES,
        'tamanhos': Animal.TAMANHO_CHOICES,
    }
    
    return render(request, 'enciclopet.html', context)

def detalhes_animal(request, id):
    # Busca o animal pelo ID. Se não achar, mostra a tela de Erro 404
    animal = get_object_or_404(Animal, id=id)
    
    # Puxa as fotos extras que cadastramos naquele "quadro" do admin
    fotos_extras = animal.fotos_adicionais.all()
    
    context = {
        'animal': animal,
        'fotos_extras': fotos_extras,
    }
    return render(request, 'detalhes_animal.html', context)