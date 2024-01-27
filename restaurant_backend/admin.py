from django.contrib import admin
from .models import (
    Customer,
    Employee,
    Order,
    OrderItem,
    MenuItem,
    Table,
    Reservation
)

admin.site.register([Customer,
    Employee,
    Order,
    OrderItem,
    MenuItem,
    Table,
    Reservation])