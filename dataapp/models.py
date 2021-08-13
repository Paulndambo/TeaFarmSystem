from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Binary", "Binary"),
)

POSITION_CHOICES = (
    ("Director", "Director"),
    ("Manager", "Manager"),
    ("Technician", "Technician"),
    ("Clerk", "Clerk"),
    ("Accountant", "Accountant"),
)

SHIFT_CHOICES = (
    ("Day", "Day"),
    ("Night", "Night"),
    ("Full-Time", "Full-Time"),
)

MONTH_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

YEAR_CHOICES = (
    (2021, 2021),
    (2022, 2022),
    (2023, 2023),
    (2024, 2024),
    (2025, 2025),
    (2026, 2026),
    (2027, 2027),
    (2028, 2028),
    (2029, 2029),
    (2030, 2030),
)

class Staff(models.Model):
    id_number = models.CharField(max_length=20, unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, choices=POSITION_CHOICES)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=200, unique=True)
    shift = models.CharField(max_length=50, choices=SHIFT_CHOICES)
    postal_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    county_or_state_or_region = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    employment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("staff")

class Farmer(models.Model):
    id_number = models.CharField(max_length=20, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=200, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    postal_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    join_date = models.DateField(default=timezone.now)
    join_year = models.IntegerField(choices=YEAR_CHOICES, default=timezone.now().year)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("farmers")

TEA_PRICE_CHOICES = [
    ("Grade 1", (
        (230, 230),
        )
    ),
    ("Grade 2", (
        (150, 150),
        )
    ),
]

class Delivery(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    unit_price = models.IntegerField(choices=TEA_PRICE_CHOICES, default=150)
    delivery_date = models.DateField(default=timezone.now)
    month = models.CharField(max_length=200, choices=MONTH_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)
    recorded_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.farmer.user.username

    def get_absolute_url(self):
        return reverse("deliveries")

class Billing(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    total_quantity_delivered = models.FloatField(default=0)
    total_cumulative_amount = models.FloatField(default=0)
    amount_paid = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    year = models.IntegerField(choices=YEAR_CHOICES, default=2021)

    def __str__(self):
        return self.farmer.user.username

    def get_balance(self):
        return self.total_cumulative_amount - self.amount_paid

class PayFarmer(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    year = models.IntegerField(choices=YEAR_CHOICES)

    def __str__(self):
        return self.farmer.user.username

    def get_absolute_url(self):
        return reverse("farmer-payments")
