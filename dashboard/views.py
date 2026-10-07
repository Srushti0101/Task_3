from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    context = {
        'stats': [
            {'title': 'Total Users', 'value': 1250, 'icon': '👥'},
            {'title': 'Total Sales', 'value': '₹45,000', 'icon': '💰'},
            {'title': 'New Orders', 'value': 87, 'icon': '📦'},
            {'title': 'Messages', 'value': 14, 'icon': '✉️'},
        ],
        'orders': [
            {'id': '#1001', 'customer': 'Amit', 'amount': '₹1,200', 'status': 'Delivered'},
            {'id': '#1002', 'customer': 'Priya', 'amount': '₹850', 'status': 'Pending'},
            {'id': '#1003', 'customer': 'Rahul', 'amount': '₹2,300', 'status': 'Delivered'},
            {'id': '#1004', 'customer': 'Sneha', 'amount': '₹640', 'status': 'Pending'},
        ],
    }
    return render(request, 'dashboard.html', context)