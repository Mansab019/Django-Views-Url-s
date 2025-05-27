from django.urls import path #re_path
from . import views


urlpatterns = [
    # re_path(r"^(?i)(?P<month>[a-zA-Z]+)/$", views.monthly_challanges, name="month-challange"),
    # re_path(r"^(?i)(?P<month>[a-zA-Z]+)/$", views.monthly_challenge, name="month-challenge"),  
    path("",views.index),     
    path("<int:month>", views.monthly_challanges_By_num),
    path("<str:month>", views.monthly_challanges, name = "month-challange")
]
