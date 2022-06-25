from django.urls import path, include

from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
    path('portfolios/', views.portfolios, name="portfolios"),
    path('portfolio/<str:pk>/', views.portfolio, name="portfolio"),
    path('delete_portfolio/<str:pk>/', views.deletePortfolio, name="delete_portfolio"),
    path('insert_identifier/', views.insertIdentifier, name="update_identifier"),
    path('update_identifier/<str:pk>/', views.updateIdentifier, name="update_identifier"),
    path('delete_identifier/<str:pk>/', views.deleteIdentifier, name="delete_identifier"),
    path('portfolio/<str:pk>/json/', views.portfolio_json, name="portfolio_json"),
    path('bulk_delete/', views.bulk_delete, name="bulk_delete"),
    path('bulk_edit/', views.bulk_edit, name="bulk_edit"),
]
