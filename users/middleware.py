from django.conf import settings
from django.shortcuts import render


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        maintenance_mode = getattr(settings, "MAINTENANCE_MODE", False)
        if maintenance_mode:
            return render(request, "maintenance.html")
        return self.get_response(request)
