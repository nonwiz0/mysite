
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('aiuts/', include('aiuts.urls')),
    path('note_keeper/', include('note_keeper.urls')),
]
