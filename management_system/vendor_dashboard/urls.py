from django.urls import path
from .views import RegisterVendorView, VendorLoginView, DashboardView, QuotationsView

urlpatterns = [
    path('register/', RegisterVendorView.as_view(), name='vendor_registration'),
    path('login/', VendorLoginView.as_view(), name='vendor_login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('quotations/', QuotationsView.as_view(), name='quotations'),
    # Add other URL patterns as needed
]
