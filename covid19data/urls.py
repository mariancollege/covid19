from django.urls import path,include
from covid19data import views

urlpatterns=[
    path('covid19/',views.test),
    path('',views.test),
]
