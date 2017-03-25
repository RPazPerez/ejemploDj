from django.conf.urls import url
from app.hackaton import views

urlpatterns = [
    url(r'^$', views.login_view, name="login_view"),
    url(r'^login/autentificar$', views.login_aut, name="login_aut"),
    url(r'^registro$', views.registro_view, name="registro_view"),
    url(r'^registro/registrar$', views.registro_registrar, name="registro_registrar"),
    url(r'^index$', views.index_view, name="index_view"),
    url(r'^profile$', views.profile_view, name="profile_view"),
    url(r'^profile/modificar$', views.profile_view_modificar, name="profile_view_modificar"),
]
