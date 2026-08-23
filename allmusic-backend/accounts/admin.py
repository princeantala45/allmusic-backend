from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Device


class DeviceInline(admin.TabularInline):

    model = Device

    extra = 0

    fields = (
        "device_name",
        "browser",
        "operating_system",
        "ip_address",
        "status",
        "created_at",
        "approved_at",
        "last_seen",
    )

    readonly_fields = (
        "device_name",
        "browser",
        "operating_system",
        "ip_address",
        "created_at",
        "approved_at",
        "last_seen",
    )


class CustomUserAdmin(UserAdmin):

    inlines = [
        DeviceInline
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.action(description="Approve selected devices")
def approve_devices(modeladmin, request, queryset):

    queryset.update(
        status="approved",
        approved_at=timezone.now()
    )


@admin.action(description="Reject selected devices")
def reject_devices(modeladmin, request, queryset):

    queryset.update(
        status="rejected"
    )


@admin.action(description="Revoke selected devices")
def revoke_devices(modeladmin, request, queryset):

    queryset.update(
        status="pending",
        approved_at=None
    )


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "device_name",
        "browser",
        "operating_system",
        "ip_address",
        "status",
        "created_at",
        "approved_at",
        "last_seen",
    )

    list_filter = (
        "status",
        "browser",
        "operating_system",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "device_name",
        "device_id",
        "ip_address",
    )

    readonly_fields = (
        "device_id",
        "created_at",
        "approved_at",
        "last_seen",
    )

    actions = [
        approve_devices,
        reject_devices,
        revoke_devices,
    ]