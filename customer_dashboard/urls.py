from django.urls import path
from .views import AddFormView, CustomerLoginView, CustomerDashboardView

urlpatterns = [
    path('', AddFormView.as_view(), name='add_form'),
    path('customer-login/', CustomerLoginView.as_view(), name='customer_login'),
    path('customer-dashboard/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    # Add other URLs as needed
]
