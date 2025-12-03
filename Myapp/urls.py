from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path("increase-visitor", views.increase_visitor, name="increase_visitor"),
]