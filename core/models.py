from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Categorias"

class Produto(models.Model):
    # Foto de capa (aparece primeiro)
    imagem_capa = models.ImageField(upload_to='produtos/capas/', verbose_name='Foto de Capa')
    
    nome = models.CharField(max_length=100)
    sku = models.CharField(max_length=20, unique=True, verbose_name='SKU (Código)')
    descricao = models.TextField(verbose_name='Descrição Detalhada', blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    
    # Categoria (o botão de + aparecerá automaticamente no admin)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos')
    
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    @property
    def preco_10x(self):
        return self.preco / 10

class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='imagens_extras')
    imagem = models.ImageField(upload_to='produtos/galeria/')
    
    def __str__(self):
        return f"Imagem de {self.produto.nome}"
    
