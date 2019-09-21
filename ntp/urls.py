from django.urls import path, include 
from  .views import NotifyViewSet
from rest_framework import routers

router=routers.DefaultRouter()
routers=router.register(r'', NotifyViewSet )


urlpatterns=[
    path('', include(router.urls) )
]