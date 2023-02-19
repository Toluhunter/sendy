from django.urls import path
from . import views

urlpatterns = [
    path("", views.FakeView.as_view())
]