from django.conf.urls import url

from crwalling import views

urlpatterns = {
    url(r'^today', views.today_detail),
    url(r'^week', views.week_detail),
}