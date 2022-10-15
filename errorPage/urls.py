from django.urls import path
from . import views
#Error page urls


urlpatterns = [
    path('404/', views.errorPage, name="error")

]
