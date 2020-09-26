from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter


from profiles.api.views import ProfileListAPIView, ProfileStatusModelViewSet, ProfileAvatarUpdateAPIView

app_name = 'profiles'

router = DefaultRouter()
router.register(r'profiles', ProfileListAPIView, 'list')
router.register(r'status', ProfileStatusModelViewSet, 'status')

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', ProfileAvatarUpdateAPIView.as_view(), name='avatar'),
]