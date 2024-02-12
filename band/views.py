# band/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Band, MembershipType, Membership, CommonFields
from .serializers import BandSerializer, MembershipTypeSerializer, MembershipSerializer, CommonFieldsSerializer

class BandListView(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class BandDetailView(generics.RetrieveAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class JoinBandView(generics.CreateAPIView):
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        band_id = self.kwargs.get('band_id')
        band = Band.objects.get(id=band_id)
        user = self.request.user
        data = {
            'user': user.id,
            'band': band.id,
            'preferred_payment_type': request.data.get('preferred_payment_type'),
            'membership_type': request.data.get('membership_type'),
            # Add other fields as needed
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommonFieldsView(generics.RetrieveUpdateAPIView):
    serializer_class = CommonFieldsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return CommonFields.objects.get_or_create(user=user)[0]

class MembershipTypeListView(generics.ListAPIView):
    serializer_class = MembershipTypeSerializer
    permission_classes = [IsAuthenticated]  # Enforce authentication

    def get_queryset(self):
        band_id = self.kwargs.get('band_id')
        user = self.request.user  # Assuming the user is authenticated

        # Filter MembershipType objects based on the band_id and user
        return MembershipType.objects.filter(band_id=band_id, memberships__user=user).distinct()
    
class MembershipTypeDetailView(generics.RetrieveAPIView):
    queryset = MembershipType.objects.all()
    serializer_class = MembershipTypeSerializer
    permission_classes = [IsAuthenticated]  # Enforce authentication
