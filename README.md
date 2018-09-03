# DjangoBlogApplication

Vejamos que adicionar o comando: 

````bash
# para abrir as configurações para fazer o administrador
django-admin < comandos > s

cd django_project

````

| Comandos | Descrição |
| -------- | --------- | 
| `startproject <nome_projeto>` | vai iniciar um novo projeto |

### Estrutura da aplicação (*inicio*)

````
|---- <nome_aplicação>  ( nome da aplicação )
    |--- migrations
        | --- __init__.py
    |--- __init__.py (dizendo que é uma estrutura python)
    |--- admin.py
    |--- apps.py
    |--- models.py
    |--- tests.py
    |--- views.py
|---- <nome_projeto>
    |---- __init__.py 
    |---- settings.py ( o vai fazer as configurações )
    |---- urls.py ( rotas e o mapeamento )
    |---- wsgi.py ( aplicação web e aplicação djson, vão se comunicar )
|---- manange.py (vai permitir executar os comandos)
````

### @Comando `manage.py`

Você utiliza o manage, para fazer todo o gerenciamento da aplicação, com isso tu pode fazer.

````bash
python manage.py startapp <nome_app> s
````

| Comandos | Descrição |
| -------- | --------- | 
| `startapp <nome_app>` | inicia uma nova aplicação |