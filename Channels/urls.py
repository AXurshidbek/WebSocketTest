from django.contrib import admin
from django.urls import path
from navbat.views import *
urlpatterns = [
            path('admin/', admin.site.urls),
            path('person-post/', PersonPostAPI.as_view()),
]
