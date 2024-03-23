from django.urls import path
from .views import AddFormView, CustomerLoginView

urlpatterns = [
    path('add-form/', AddFormView.as_view(), name='add_form'),
    path('customer-login/', CustomerLoginView.as_view(), name='customer_login'),
    # Add other URLs as needed
]
