from django.urls import path
from . import views
#home page urls


urlpatterns = [
    path('main/', views.homePage, name="home")

]
