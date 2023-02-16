from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>',views.home_page,name="main_home" )

]