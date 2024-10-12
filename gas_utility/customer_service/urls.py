from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('submit-request/', views.submit_request, name='submit_request'),
    path('my-requests/', views.request_list, name='request_list'),
    path('manage-requests/', views.manage_requests, name='manage_requests'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
    path('admin/', admin.site.urls),
    path('customer/', include('customer_service.urls')),
]
