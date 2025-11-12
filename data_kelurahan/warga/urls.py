from django.urls import path
from .views import WargaListView, PengaduanListView  # tambahkan PengaduanListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),  # tambahkan ini
]
