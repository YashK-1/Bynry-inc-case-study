from django.urls import path
from . import views

urlpatterns = [
    path('submit-request/', views.submit_request, name='submit_request'),
    path('my-requests/', views.request_list, name='request_list'),
    path('manage-requests/', views.manage_requests, name='manage_requests'),
]
