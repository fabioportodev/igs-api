
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .core.views import DepartamentList, EmployeeViewSet


router = routers.DefaultRouter()

router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('departaments/', DepartamentList.as_view()),
    path('admin/', admin.site.urls),
]
