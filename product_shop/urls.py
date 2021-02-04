from . import views
from django.urls import path


urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('detail_product/<int:pk>/', views.ProductView.as_view(), name='detail_product'),
    path('filter/<int:category_id>/', views.filter_by_category, name='filter_by_category'),
    path('create_post/', views.CreateProduct.as_view(), name='create_post'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_post'),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),

]