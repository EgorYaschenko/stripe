from django.urls import path
from .views import item_index, Index, CreateCheckoutSessionView, CancelView,  SuccessView

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('Item/<int:id>/', item_index, name='item'),
    path('', Index, name='Index'),

]
