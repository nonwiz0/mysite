from django.urls import path

from . import views

app_name = 'note_keeper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_note/', views.create_note, name='create_note'),
    path('<str:note_title>/delete_note/', views.delete_note, name='delete_note'),
    path('<str:pk>/', views.DetailView.as_view(), name='note'),
    path('<str:pk>/edit', views.EditView.as_view(), name='edit_note'),
    path('update_note', views.update_note, name='update_note')
]

