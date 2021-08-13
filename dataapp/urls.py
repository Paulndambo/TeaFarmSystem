from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.farmer_profile, name="profile"),
    path("farmers/", FarmersList.as_view(), name="farmers"),
    path("record-farmer/", RecordFarmer.as_view(), name="record-farmer"),
    path("update-farmer/<int:pk>/", UpdateFarmer.as_view(), name="update-farmer"),
    path("farmer-details/<int:pk>/", FarmerDetails.as_view(), name="farmer-details"),
    path("delete-farmer/<int:pk>/", DeleteFarmer.as_view(), name="delete-farmer"),
    path("staff/", StaffList.as_view(), name="staff"),
    path("record-staff/", RecordStaff.as_view(), name="record-staff"),
    path("update-staff/<int:pk>/", UpdateStaff.as_view(), name="update-staff"),
    path("staff-details/<int:pk>/", StaffDetails.as_view(), name="staff-details"),
    path("delete-staff/<int:pk>/", DeleteStaff.as_view(), name="delete-staff"),
    path("deliveries/", DeliveryList.as_view(), name="deliveries"),
    path("record-delivery/", RecordDelivery.as_view(), name="record-delivery"),
    path("delete-delivery/<int:pk>/", DeleteDelivery.as_view(), name="delete-delivery"),
    path("billing/", BillingList.as_view(), name="billing"),
    path("farmer-payments/", PaymentList.as_view(), name="farmer-payments"),
    path("pay-farmer/", PayFarmerBill.as_view(), name="pay-farmer"),
]
