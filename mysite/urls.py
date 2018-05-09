from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from radar import views

router = routers.DefaultRouter()
router.register(r'societies', views.SocietyViewSet)
router.register(r'events', views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

