from django.contrib import admin
from django.urls import path
from rest_framework import routers
from mymessages.views import MessageViewSet
from contacts.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r"messages", MessageViewSet)
router.register(r"contacts", ContactViewSet)

urlpatterns = [

    path("admin/", admin.site.urls),
]
