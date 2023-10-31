from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mymessages.views import MessageViewSet
from contacts.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r"messages", MessageViewSet)
router.register(r"contacts", ContactViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/messages', include('mymessages.urls')),
    path('api/contacts', include('contacts.urls')),
]
