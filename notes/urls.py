from django.urls import path

from . import views

urlpatterns = [
    path('removenote/<int:note_id>/', views.removenote ),
    path('editnote/<int:note_id>/', views.removenote ),
    path('', views.addnote, name='index'),
]
