from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
LISTA_CATEGORIAS = (
    ("ANALISE" , "Análise"),
    ("APRESENTACAO" , "Apresentação"),
    ("PROGRAMACAO" , "Programação"),
    ("OUTROS" , "Outros")
)
# Criar o modelo da pagina filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=15 , choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# Criar o modelo da pag epsodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme" , related_name="episodios" , on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


# Criar o modelo da pagina usuário


class Usuario(AbstractUser):
    filme_vistos = models.ManyToManyField("Filme")

