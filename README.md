# 🌿 Modern Green E-commerce BETA
> *Onde o Django mostra sua elegância com Designs Modernos.*

Seja bem-vindo(a) ao repositório! Este projeto nasceu da ideia de criar uma loja virtual que fugisse do visual padrão e "quadrado" dos sistemas administrativos comuns. Aqui, o foco foi unir um **Back-end (Python/Django)** com uma experiência de usuário **(Front-end)** fluida, minimalista e agradável. e por fim liberar uma versão em codigo aberto e ser feitas modificações para um projeto de loja inicial.

![Status do Projeto](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)

---

## 🎨 Proposta Visual
O desafio principal aqui foi: *"Como deixar um sistema complexo com cara de aplicativo moderno?"*
Para isso, utilizei uma paleta de cores inspirada na natureza (Verdes sóbrios, Brancos e detalhes em Amarelo), abusei de bordas arredondadas (estilo "pill-shape") e criei interações suaves.

*(Espaço reservado para um print ou GIF da interface)*

---

## 🚀 O que tem de legal aqui?

Não é apenas uma vitrine bonita, o sistema tem "cérebro". Abaixo, algumas funcionalidades que implementei:

### 🧠 Busca "Ao Vivo" (Live Search)
Sabe quando você começa a digitar e o site já adivinha o que você quer? Implementei isso usando **JavaScript e AJAX**. O sistema conversa com o Django em tempo real e te mostra a foto e o preço do produto antes mesmo de você apertar "Enter". (Muito importante para a experiencia do usuario.)

### 🛍️ Experiência de Compra
* **Vitrine Inteligente:** Os produtos já mostram o cálculo de parcelamento (10x) automaticamente.
* **Galeria Interativa:** Na página do produto, você pode navegar pelas fotos com setas ou clicando nas miniaturas. Tudo feito à mão, sem plugins pesados.
* **Menu Lateral Imersivo:** Um menu que desliza suavemente e foca a atenção do usuário escurecendo o fundo.

### 🛡️ Painel Administrativo (Mas não o padrão!)
Eu não queria entregar aquele admin azul padrão do Django. Utilizei a biblioteca *Jazzmin* e personalizei o CSS para que o painel de controle tivesse **a mesma identidade visual do site**.
* Gestão completa de produtos (com upload de múltiplas fotos).
* Criação dinâmica de categorias.
* **Limpeza Automática:** Se você deletar um produto, o sistema varre a pasta de mídia e apaga as fotos dele para não ocupar espaço à toa no servidor.

---

## 🛠️ Tecnologias que fizeram acontecer

* **O Motor:** Python 3 + Django Framework.
* **A Cara:** HTML5, CSS3 (com Variáveis CSS) e JavaScript Puro (Vanilla).
* **O Banco:** SQLite (leve e perfeito para desenvolvimento).
* **Bibliotecas Chave:**
    * `Pillow`: Para tratar as imagens.
    * `django-cleanup`: Para manter a casa limpa (apagar arquivos não usados).
    * `django-jazzmin`: Para deixar o admin bonitão.

---

## ⚙️ Quer rodar na sua máquina?

Fique à vontade para clonar, testar e fuçar no código!

## 1. Instale o que precisa
`pip install -r requirements.txt`
## 2. Prepare o Banco de Dados
`python manage.py makemigrations`
`python manage.py migrate`
## 3. Crie seu usuário Admin para acessar o painel e cadastrar os produtos:
`python manage.py createsuperuser`
## 4. Por fim
`python manage.py runserver`