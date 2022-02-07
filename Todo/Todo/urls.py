
from django.contrib import admin
from django.urls import path, include
from app1.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("todo",TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
