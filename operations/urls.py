from django.urls import path
from . import views


urlpatterns = [
    path("operations/", views.OperationView.as_view()),
]
