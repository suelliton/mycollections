from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.login),
    url(r'^index/$',views.index),
    url(r'^index/logout/$',views.logout),
    url(r'^excluirVideo/$',views.excluirVideo),
    url(r'^filtraVideo/$',views.filtraVideo),
    url(r'^filtraVideo/logout/$',views.logout),
    url(r'^cadastra_usuario/$',views.cadastra_usuario),



]
