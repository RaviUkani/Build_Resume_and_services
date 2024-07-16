from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home-saved'),
    path("contact/", views.contact, name='contact-saved'),
]
