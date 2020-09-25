from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
