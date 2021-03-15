from django.urls import path

from . import views

app_name = 'note_keeper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_note/', views.create_note, name='create_note'),
    path('<int:note_id>/delete_note/', views.delete_note, name='delete_note'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/reset_vote/', views.reset_vote, name='reset_vote'),
]

