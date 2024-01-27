from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=50)
    contact_info = models.TextField()
    schedule = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50, default='Uncategorized')

    def __str__(self):
        return f"{self.name}: {self.description} - {self.price}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    table_number = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order for {self.customer.first_name} {self.customer.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    special_instructions = models.TextField(blank=True)

class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, null=True)
    reservation_time = models.DateTimeField(default=timezone.now)
    number_of_guests = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, default=None, null=True)

    def __str__(self):
        return f"Reservation for {self.customer.first_name} {self.customer.last_name} at {self.reservation_time}"
