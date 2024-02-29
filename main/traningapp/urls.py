from django.urls import path
from .views import ProductListAPIView, LessonsForProductALIVew


urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:product_id>/lessons/', LessonsForProductALIVew.as_view(), name='lessons_product'),

]
