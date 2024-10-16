from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customer_service/request_list.html', {'requests': requests})

# For admin/staff
@login_required
def manage_requests(request):
    if request.user.is_staff:
        requests = ServiceRequest.objects.all()
        return render(request, 'customer_service/manage_requests.html', {'requests': requests})
    return redirect('home')

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('track_request')  # Redirect after successful submission
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def track_request(request):
    service_requests = ServiceRequest.objects.filter(customer__email=request.user.email)
    return render(request, 'track_request.html', {'requests': service_requests})

def manage_requests(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'manage_requests.html', {'requests': service_requests})
