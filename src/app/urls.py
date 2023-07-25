from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
]