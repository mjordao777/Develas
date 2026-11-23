from django.contrib import admin 

from django.urls import path 

 

from vagas import views 

 

urlpatterns = [ 

    path("admin/", admin.site.urls), 

    path("", views.home, name="home"), 

    path("sobre/", views.sobre, name="sobre"), 

    path("vagas/", views.mural, name="mural"), 

    path("vagas/<int:vaga_id>/", views.detalhe, name="detalhe"), 

    path("contato/", views.contato, name="contato"), 

] 



