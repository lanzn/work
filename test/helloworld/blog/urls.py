from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^extent1', views.extent1, name='extent1'),
  url(r'^extent2', views.extent2, name='extent2'),
  
]