from django.urls import path
from . import views

urlpatterns = [
    path('platform/news/', views.news_view, name='news'),
]
