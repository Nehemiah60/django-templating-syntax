from django.urls import path
from .views import (
    create_new_products,
    product_update_view,
    dynamic_lookup_view, 
    product_delete_view, 
    product_list_view,
)
     
app_name = "Product"
urlpatterns = [
      path('create/', create_new_products),
      path('<int:my_id>/', dynamic_lookup_view, name="product-detail"),
      path('<int:my_id>/update/', product_update_view, name="product-update"),
      path('<int:my_id>/delete/', product_delete_view, name="product-delete"),
      path('', product_list_view, name='proudct-list'),

]
