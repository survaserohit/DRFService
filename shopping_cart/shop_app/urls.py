from django.urls import path
from .views import CartItemViews

urlpatterns=[
    path("cart-items/<int:id>",CartItemViews.as_view())
]