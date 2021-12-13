"""gameturbo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from locadora.views import home, form, create
from locadora.views import view, edit, update, delete
from locadora.views import formjogo, createjogo, viewjogo
from locadora.views import editjogo, updatejogo, deletejogo
from locadora.views import listarcliente, listarjogo





urlpatterns = [
    #cliente
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('form/', form, name='form'),  
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('listarcliente/', listarcliente, name='listarcliente'),
    #jogo
    path('formjogo/', formjogo, name='formjogo'),
    path('createjogo/', createjogo, name='createjogo'),
    path('viewjogo/<int:pk>/', viewjogo, name='viewjogo'),
    path('editjogo/<int:pk>/', editjogo, name='editjogo'),
    path('updatejogo/<int:pk>/', updatejogo, name='updatejogo'),
    path('deletejogo/<int:pk>/', deletejogo, name='deletejogo'),  
    path('listarjogo/', listarjogo, name='listarjogo')

    
]