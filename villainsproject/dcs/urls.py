from django.urls import path
from .views import DcList, DcDetail, DcCreate, DcUpdate, DcDelete, DcCoverCreate, DcinfoCreate, DcCoverCreate, DcinfoCreate

urlpatterns = [
    path('', DcList.as_view(), name='dcs-home'),
    path('<int:pk>', DcDetail.as_view(), name='dc-detail'),
    path('add', DcCreate.as_view(), name='add-dc'),
    path('edit/<int:pk>', DcUpdate.as_view(), name='edit-dc'),
    path('delete/<int:pk>', DcDelete.as_view(), name='delete-dc'),
    path('dccover/add/<int:pk>', DcCoverCreate.as_view(), name='add-dccover'),
    path('dcinfo/add/<int:pk>', DcinfoCreate.as_view(), name='add-dcinfo'),
]