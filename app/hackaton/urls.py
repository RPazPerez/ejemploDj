from django.conf.urls import url
from app.hackaton import views

urlpatterns = [
    url(r'^$', views.login_view, name="login_view"),
    url(r'^login/autentificar$', views.login_aut, name="login_aut"),
    url(r'^registro$', views.registro_view, name="registro_view"),
    url(r'^index$', views.index_view, name="index_view"),
]
