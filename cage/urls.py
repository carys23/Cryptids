from django.urls import path
from .views import SearchResutlsView, HomepageView

urlpatterns = [
    path('search/', SearchResutlsView.as_view(). name='search_results'),
    path('',Homepageview.as_view(), name='home')
]