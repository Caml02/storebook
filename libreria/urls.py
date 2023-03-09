from django.urls import path 
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('books', views.books, name='books'),
    path('books/crear', views.crear, name='crear'),
    path('books/editar', views.editar, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('books/editar/<int:id>', views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)