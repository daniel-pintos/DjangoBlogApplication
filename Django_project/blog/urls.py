from django.urls import path

from . import views

"""
    O que tem que ser passado é basicamente:
        * caminho - {""} - vazio é igual a home
        * função - {você pega das variáveis de view's }
        * name - 'que seria uma tag para que ele consiga se localizar'
        * parametros 
    O que pode fazer é deixar sem o /, que ele vai colocar.
"""
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
