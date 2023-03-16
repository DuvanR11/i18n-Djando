"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

# Asi es para que aparezca en la url /es/ o /en/ con este testo
urlpatterns = i18n_patterns(
    path('', include('myapp.urls')),
)

# Naeku trabaja de esta forma y el language_code se va por cookie justas sirven igual
# urlpatterns = [
#     path('', include('myapp.urls')),
# ]
