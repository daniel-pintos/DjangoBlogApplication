from django.shortcuts import render

# Create your views here.


"""
O que vai ser a rota para home.
@:param request (requisição)  

a função `render`:
    1. request
    2. template
    3. argumentos

@Render > procura no diretorio templates, a renderização.
    # Funcionamento:
        blog --> templates --> blog --> templates.html
"""

posts = [
    {'author': "CoreyMS", 'title': "Blog Post 1", "content": "First post content", "date_posted": 'August 27, 2018'},
    {'author': "CoreyMS", 'title': "Blog Post 2", "content": "Second post content", "date_posted": 'August 28, 2018'},
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
