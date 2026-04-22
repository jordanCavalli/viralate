from django.db import models
from django.core.exceptions import ValidationError

class Parceiro(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='parceiros/')
    area_atuacao = models.CharField(max_length=100, verbose_name="Área de Atuação")
    contato = models.CharField(max_length=100, help_text="Pode ser WhatsApp, Instagram ou Telefone")
    link_site = models.URLField(blank=True, null=True, help_text="Link opcional para site ou rede social")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"

    
class Animal(models.Model):
    ESPECIE_CHOICES = [
        ('CACHORRO', 'Cachorro'),
        ('GATO', 'Gato'),
    ]

    TAMANHO_CHOICES = [
        ('PEQUENO', 'Pequeno'),
        ('MEDIO', 'Médio'),
        ('GRANDE', 'Grande'),
    ]

    SEXO_CHOICES = [
        ('MACHO', 'Macho'),
        ('FEMEA', 'Fêmea'),
    ]

    STATUS_CHOICES = [
        ('ADOTAR', 'Para Adoção'),
        ('PERDIDO', 'Perdido'),
        ('ENCONTRADO', 'Encontrado'),
    ]

    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='animais/')
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    idade = models.CharField(max_length=50, help_text="Ex: 2 anos, Filhote (3 meses)")
    tamanho = models.CharField(max_length=20, choices=TAMANHO_CHOICES, blank=True, null=True, help_text="Deixe em branco se for gato")
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ADOTAR')
    
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Meta:
        # Define o nome no singular e no plural para o Admin
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

def __str__(self):
        return f"{self.nome} ({self.get_especie_display()})"

from django.db import models

class Animal(models.Model):
    ESPECIE_CHOICES = [
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
    ]
    
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
    ]

    # Os valores à esquerda (ADOTAR, PERDIDO...) precisam ser iguais ao CSS
    STATUS_CHOICES = [
        ('ADOTAR', 'Para Adotar'),
        ('PERDIDO', 'Perdido'),
        ('ENCONTRADO', 'Encontrado'),
    ]

    TAMANHO_CHOICES = [
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
    ]

    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='animais/')
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    # Adicionamos o default para sumir com o espaço em branco no Admin
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='ADOTAR'
    )
    
    tamanho = models.CharField(
        max_length=20, 
        choices=TAMANHO_CHOICES, 
        blank=True, 
        null=True
    )
    
    idade = models.CharField(max_length=50)
    historia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.especie == 'Gato' and self.tamanho:
            raise ValidationError({
                'tamanho': 'Gatos não devem ter o campo "Tamanho" preenchido.'
            })
class AnimalFoto(models.Model):
    animal = models.ForeignKey(Animal, related_name='fotos_adicionais', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='animais/galeria/')