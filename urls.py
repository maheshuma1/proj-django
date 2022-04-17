from django.urls import path
from .views import jsonView

urlpatterns = [
    path("", jsonView, name="home"),
]