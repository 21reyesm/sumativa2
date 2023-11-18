
from django.urls import path
from .views import lista_publicaciones, blog_home, detalle_publicacion

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('publicacion/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    path('', lista_publicaciones, name='lista_publicaciones'),
]
