
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),     
    
    # TO DO
    path('todo/', include('todo.urls')), 
]