from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='shop-home'),
    path("cart/",views.cart,name='shop-cart'),
    path("checkout/",views.checkout,name='shop-checkout'),
    path('addtocart/<int:pk>',views.addtocart,name="addtocart"),
    path('delete/<int:pk>',views.delete_cart_item,name='delete-cart-item'),
    path('productview/<int:pk>',views.product_view,name='product-view'),
    path('search/',views.search,name='search'),
    path('category/<str:category>',views.category,name="category")
]

