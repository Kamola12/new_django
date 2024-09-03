from django.urls import path
from .views import HomePageView,ProductView,ProductDetailView

urlpatterns = [
    path('', HomePageView.as_view(),name="home"),
    path('products/', ProductView.as_view(),name="products"),
    path('products/<int:id>/', ProductDetailView.as_view(),name="detail"),
]
