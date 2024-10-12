from django.contrib.auth.models import User
from django.db import models

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    request_type = models.CharField(max_length=100)  # E.g. Gas Leak, Maintenance, etc.
    description = models.TextField()
    file_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('resolved', 'Resolved')], default='pending')
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.username} - {self.request_type}"

# Extend the user model for more customer info (optional)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)