from django.urls import path
from .views import MarvelList, MarvelDetail, MarvelCreate, MarvelUpdate, MarvelDelete, MarvelCoverCreate, MarvelinfoCreate, MarvelCoverCreate, MarvelinfoCreate

urlpatterns = [
    path('', MarvelList.as_view(), name='marvels-home'),
    path('<int:pk>', MarvelDetail.as_view(), name='marvel-detail'),
    path('add', MarvelCreate.as_view(), name='add-marvel'),
    path('edit/<int:pk>', MarvelUpdate.as_view(), name='edit-marvel'),
    path('delete/<int:pk>', MarvelDelete.as_view(), name='delete-marvel'),
    path('marvelcover/add/<int:pk>', MarvelCoverCreate.as_view(), name='add-marvelcover'),
    path('marvelinfo/add/<int:pk>', MarvelinfoCreate.as_view(), name='add-marvelinfo'),
]