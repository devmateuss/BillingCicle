from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from BillingCicle import views

router = routers.DefaultRouter()
router.register(r'billingcicle', views.BillingCicleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
