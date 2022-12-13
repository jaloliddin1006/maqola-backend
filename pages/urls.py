from django.urls import path
from .views import HomePageView,ContactView
urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('/contact', ContactView, name = 'contact')
]