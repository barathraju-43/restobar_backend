from django.http import JsonResponse
from .models import (
    Customer,
    Employee,
    Order,
    OrderItem,
    MenuItem,
    Table,
    Reservation
)
from .serializers import (
    CustomerSerializer,
    EmployeeSerializer,
    OrderSerializer,
    MenuItemSerializer,
    OrderItemSerializer,
    TableSerializer,
    ReservationSerializer,
)

def CustomerList(request):
    menuitems = Customer.objects.all()
    serializer = CustomerSerializer(menuitems, many=True)
    return JsonResponse(serializer.data, safe=False)

def EmployeeList(request):
    orderitems = Employee.objects.all()
    serializer = EmployeeSerializer(orderitems, many=True)
    return JsonResponse(serializer.data, safe=False)

def OrderItemList(request):
    menuitems = OrderItem.objects.all()
    serializer = OrderItemSerializer(menuitems, many=True)
    return JsonResponse(serializer.data, safe=False)

def TableList(request):
    orderitems = Table.objects.all()
    serializer = TableSerializer(orderitems, many=True)
    return JsonResponse(serializer.data, safe=False)

def ReservationList(request):
    orderitems = Reservation.objects.all()
    serializer = ReservationSerializer(orderitems, many=True)
    return JsonResponse(serializer.data, safe=False)

def MenuItemList(request):
    menuitems = MenuItem.objects.all()
    serializer = MenuItemSerializer(menuitems, many=True)
    return JsonResponse(serializer.data, safe=False)

def OrderList(request):
    orderitems = Order.objects.all()
    serializer = OrderSerializer(orderitems, many=True)
    return JsonResponse(serializer.data, safe=False)


    
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import MenuItem, Order
# from .serializers import MenuItemSerializer, OrderSerializer

# class MenuItemList(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# class OrderList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def get(self, request, *args, **kwargs):
#         response = super().get(request, *args, **kwargs)
#         response.data['safe'] = False  # Set 'safe' to False
#         return response

    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer
