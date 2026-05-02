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
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
    ]
    
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
    ]

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

    IDADE_CHOICES = [
        ('Filhote', 'Filhote'),
        ('Adulto', 'Adulto'),
        ('Idoso', 'Idoso'),
    ]

    nome = models.CharField(max_length=100)
    
    foto = models.ImageField(
        upload_to='animais/', 
        help_text="⚠️ Recomendado: Envie uma imagem com proporção 1x1 (quadrada) para o layout ficar bonito."
    )
    
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES)
    
    idade = models.CharField(
        max_length=20, 
        choices=IDADE_CHOICES,
        default='Adulto'
    )
    
    tamanho = models.CharField(
        max_length=20, 
        choices=TAMANHO_CHOICES, 
        blank=True, 
        null=True,
        help_text="⚠️ Preencha APENAS para cachorros. Deixe em branco se for gato."
    )
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='ADOTAR'
    )
    
    historia = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.especie == 'Gato' and self.tamanho:
            raise ValidationError({
                'tamanho': 'Gatos não devem ter o campo "Tamanho" preenchido.'
            })

    def __str__(self):
        return f"{self.nome} ({self.get_especie_display()})"

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

class AnimalFoto(models.Model):
    animal = models.ForeignKey(Animal, related_name='fotos_adicionais', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='animais/galeria/')