from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^franchises/', views.franchises, name='franchise index')
]