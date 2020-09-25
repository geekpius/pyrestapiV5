from django.urls import path, re_path
from profiles.api.views import ProfileListAPIView

app_name = 'profiles'

urlpatterns = [
    path('profiles/', ProfileListAPIView.as_view(), name='list'),
]