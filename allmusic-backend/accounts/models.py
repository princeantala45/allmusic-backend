from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="devices"
    )

    device_id = models.CharField(
        max_length=255,
        unique=True
    )

    device_name = models.CharField(
        max_length=255,
        blank=True
    )

    browser = models.CharField(
        max_length=100,
        blank=True
    )

    operating_system = models.CharField(
        max_length=100,
        blank=True
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    last_seen = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Device Approval"
        verbose_name_plural = "Device Approvals"

    def __str__(self):
        return f"{self.user.username} - {self.device_name}"