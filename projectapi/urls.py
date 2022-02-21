from django.urls import path, include
from .views import *
from rest_framework import routers
from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'Project', ProjectList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('detail/<id>/', Project_detail),
]