from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

from mainapp import views

# import mainapp

app_name = 'app'

router = routers.DefaultRouter()
router.register(r'college', views.CollegeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/', obtain_jwt_token),
    path('',views.CollegeViewSet.as_view())
]