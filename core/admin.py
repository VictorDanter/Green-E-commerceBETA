from django.contrib import admin
from django.utils.html import format_html
from .models import Produto, Categoria, ImagemProduto

# Configuração para as fotos extras aparecerem DENTRO do produto
class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 1           # Começa com 1 espaço vazio
    max_num = 6         # Limita a 6 fotos extras no máximo
    verbose_name = "Foto Extra"
    verbose_name_plural = "Galeria de Fotos (Máx 6)"

class ProdutoAdmin(admin.ModelAdmin):
    # Organiza a ordem dos campos no formulário (Capa primeiro, como pediu)
    fields = ['imagem_capa', 'nome', 'sku', 'categoria', 'preco', 'descricao', 'ativo']
    
    # Adiciona a seção das fotos extras logo abaixo
    inlines = [ImagemProdutoInline]

    # Configura a lista de visualização (Grid principal)
    list_display = ('exibir_imagem', 'nome', 'sku', 'categoria', 'preco', 'ativo')
    search_fields = ('nome', 'sku')
    list_filter = ('categoria', 'ativo')
    list_editable = ('preco', 'ativo')

    # Função para mostrar uma miniatura da foto na lista geral
    def exibir_imagem(self, obj):
        if obj.imagem_capa:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 10px;" />', obj.imagem_capa.url)
        return "Sem Foto"
    
    exibir_imagem.short_description = "Capa"

# Registra tudo
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)