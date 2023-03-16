from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views


urlpatterns = [
    # ...
    path('', views.home, name="home"),   
    path('jsi18n/', JavaScriptCatalog.as_view(domain="django", packages=['myapp']), name='javascript-catalog'),
    # ...
]

# la Carpeta myproject es el proyecto django y myapp es la aplicación asi
# funciona Naeku tiene 4-5 aplicaciones en entornor de trabajo

# domain="django" hace rererencia al django.po
# packages=['myapp'] Es la aplicacion a la que se lo vamos a aplicar

# en templates esta el ejemplo de uso