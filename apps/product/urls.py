from django.urls import path, include

from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path('products/', views.products, name="products"),
    # path('portfolio/<str:pk>/', views.portfolio, name="portfolio"),
    # path('delete_portfolio/<str:pk>/', views.deletePortfolio, name="delete_portfolio"),
    # path('delete_identifier/<str:pk>/', views.deleteIdentifier, name="delete_identifier"),
]
