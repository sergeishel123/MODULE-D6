from django.urls import path
from .views import PostsList,OnePost

urlpatterns = [
    path('',PostsList.as_view()),
    path('<int:pk>',OnePost.as_view()),
]

