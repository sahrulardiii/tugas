from django.views.generic import ListView
from .models import Warga, Pengaduan  # tambahkan Pengaduan di sini

class WargaListView(ListView):
    model = Warga
    # Django secara otomatis akan mencari template di:
    # <nama_app>/<nama_model>_list.html -> warga/warga_list.html


class PengaduanListView(ListView):
    model = Pengaduan
    # Django secara otomatis akan mencari template di:
    # <nama_app>/<nama_model>_list.html -> warga/pengaduan_list.html
