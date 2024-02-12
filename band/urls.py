# band/urls.py
from django.urls import path
from .views import BandListView, BandDetailView, JoinBandView, CommonFieldsView, MembershipTypeListView, MembershipTypeDetailView

urlpatterns = [
    path('bands/', BandListView.as_view(), name='band-list'),
    path('bands/<int:pk>/', BandDetailView.as_view(), name='band-detail'),
    path('join-band/<int:band_id>/', JoinBandView.as_view(), name='join-band'),
    path('common-fields/', CommonFieldsView.as_view(), name='common-fields'),
    path('bands/<int:band_id>/membership-types/', MembershipTypeListView.as_view(), name='membership-type-list'),
    path('membership-types/<int:pk>/', MembershipTypeDetailView.as_view(), name='membership-type-detail'),
    # Add other URLs as needed
]
