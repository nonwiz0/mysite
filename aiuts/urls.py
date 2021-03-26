from django.urls import path

from . import views

app_name = 'aiuts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sign_up', views.SignupView.as_view(), name='signup'),
    path('get_balance', views.GetbalanceView.as_view(), name='getbalance'),
    path('sign_up/submit', views.create_acc, name='create_acc'),
    path('get_balance/check', views.check_balance, name="checkbalance")
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/reset_vote/', views.reset_vote, name='reset_vote'),
]