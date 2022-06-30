
from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.all_posts,name="shows_all_vacancy"),
    path('posts/<int:id>/', views.get_vacancy_detail,name="shows_vacancy_detail"),
]