from django.shortcuts import render
from . models import *
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    farmers_count = Farmer.objects.all().count()
    staff_count = Staff.objects.all().count()
    deliveries_count = Delivery.objects.all().count()
    current_year_deliveries = Delivery.objects.filter(year=timezone.now().year).count()

    context = {
        "farmers_count": farmers_count,
        "staff_count": staff_count,
        "deliveries_count": deliveries_count,
        "current_year_deliveries": current_year_deliveries
    }
    return render(request, "index.html", context)

class FarmersList(ListView):
    model = Farmer
    template_name = "farmers.html"

class RecordFarmer(CreateView):
    model = Farmer
    fields = "__all__"
    template_name = "new-farmer.html"

class UpdateFarmer(UpdateView):
    model = Farmer
    fields = "__all__"
    template_name = "update-farmer.html"

class FarmerDetails(DetailView):
    model = Farmer
    template_name = "farmer-details.html"

class DeleteFarmer(DeleteView):
    model = Farmer
    template_name = "delete-farmer.html"
    success_url = reverse_lazy("farmers")

class StaffList(ListView):
    model = Staff
    template_name = "staff.html"

class RecordStaff(CreateView):
    model = Staff
    fields = "__all__"
    template_name = "new-staff.html"

class UpdateStaff(UpdateView):
    model = Staff
    fields = "__all__"
    template_name = "update-staff.html"

class StaffDetails(DetailView):
    model = Staff
    template_name = "staff-details.html"

class DeleteStaff(DeleteView):
    model = Staff
    template_name = "delete-staff.html"
    success_url = reverse_lazy("staff")

class DeliveryList(ListView):
    model = Delivery
    template_name = "deliveries.html"

class RecordDelivery(CreateView):
    model = Delivery
    fields = "__all__"
    template_name = "add-delivery.html"

class BillingList(ListView):
    model = Billing
    template_name = "billing.html"

def farmer_profile(request):
    farmer = Farmer.objects.get(user=request.user.id)
    #deliveries = Delivery.objects.filter(farmer_id = farmer)
    #billings = Billing.objects.filter(farmer_id = farmer)

    context = {
        #"user": user,
        "farmer": farmer,
        #"deliveries": deliveries,
    }

    return render(request, "profile.html", context)

class DeliveryCreateView(CreateView):
    model = Delivery
    fields = "__all__"
    template_name = "profile.html"

class DeliveriesList(ListView):
    model = Delivery
    template_name = "profile.html"

class DeleteDelivery(DeleteView):
    model = Delivery
    template_name = "delete-delivery.html"
    success_url = reverse_lazy("deliveries")

class PayFarmerBill(CreateView):
    model = PayFarmer
    fields = "__all__"
    template_name = "pay-farmer.html"

class PaymentList(ListView):
    model = PayFarmer
    template_name = "ledger.html"