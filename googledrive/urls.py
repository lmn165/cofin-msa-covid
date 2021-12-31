from django.conf.urls import url

from googledrive import views


urlpatterns = {
    url(r'^confirmed', views.confirmed),
    url(r'^upload', views.upload),
}