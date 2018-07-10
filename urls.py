from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^today/$',views.Todays_Dues),
    url(r'^tommorow/$',views.Tommorow_Dues),
    url(r'^farm/$', views.Farm),
    url(r'^Cost/$', views.Cost),
]
