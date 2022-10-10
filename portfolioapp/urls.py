
from django.urls import path
from .views import home_page, comment_page

urlpatterns = [
    path('',home_page , name="home"),
    path("comments/",comment_page,  name="comment")

   
]
