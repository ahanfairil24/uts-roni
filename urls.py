from django.urls import path
from . import views

urlpatterns = [
    path("peminjam/", views.peminjamlistcreate.as_view(), name="peminjam-view-create"),
    path("peminjam/<int:pk>/",  views.peminjamretrieveupdatedestory.as_view(),  name='update',),
    path("pustakawan/", views.pustakawanlistcreate.as_view(), name="pustakawan-view-create"),
    path("pustakawan/<int:pk>/",  views.pustakawanretrieveupdatedestory.as_view(),  name='update',),
    path("buku/", views.bukulistcreate.as_view(), name="buku-view-create"),
    path("buku/<int:pk>/",  views.bukuretrieveupdatedestory.as_view(),  name='update',),
]
