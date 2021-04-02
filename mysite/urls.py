
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('aiuts/', include('aiuts.urls')),
    path('note_keeper/', include('note_keeper.urls')),
]
