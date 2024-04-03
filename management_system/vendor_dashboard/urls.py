from django.urls import path
from .views import RegisterVendorView, VendorLoginView, DashboardView, QuotationsView, OrdersView, InventoryView, BidView

urlpatterns = [
    path('register/', RegisterVendorView.as_view(), name='vendor_registration'),
    path('login/', VendorLoginView.as_view(), name='vendor_login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('quotations/', QuotationsView.as_view(), name='quotations'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('rfq_bids/', BidView.as_view(), name='rfq_bids'),
    # Add other URL patterns as needed
]
