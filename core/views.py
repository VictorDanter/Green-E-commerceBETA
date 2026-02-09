from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import JsonResponse
from django.db.models import Q        

def home(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'index.html', {'produtos': produtos})

# Nova função para a página de detalhes
def produto_detail(request, id):
    # Tenta buscar o produto pelo ID, se não achar, dá erro 404
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'product_detail.html', {'produto': produto})

def buscar_produtos(request):
    query = request.GET.get('q', '') # Pega o que o usuário digitou
    
    if query:
        # Filtra por Nome OU (Q) por SKU que contenha o texto (icontains = ignora maiúscula/minúscula)
        produtos = Produto.objects.filter(
            Q(nome__icontains=query) | Q(sku__icontains=query)
        ).filter(ativo=True)[:5] # Limita a 5 resultados para ser rápido
        
        # Cria uma lista de dicionários para enviar ao Javascript
        resultados = []
        for p in produtos:
            resultados.append({
                'id': p.id,
                'nome': p.nome,
                'preco': str(p.preco), # Preço precisa virar texto
                'imagem': p.imagem_capa.url if p.imagem_capa else '',
            })
        
        return JsonResponse({'results': resultados})
    
    return JsonResponse({'results': []})