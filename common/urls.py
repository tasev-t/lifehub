from django.urls import path
from .views import changelog, SnapshotView

urlpatterns = [
    path('changelog/', changelog, name='changelog'),
    path('snapshot/', SnapshotView.as_view(), name='snapshot'),
]
