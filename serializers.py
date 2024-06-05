from rest_framework import serializers
from .models import peminjam, buku, pustakawan

class peminjamserializer(serializers.ModelSerializer):
    class Meta:
        model = peminjam
        fields = ("id", "nama_peminjam", "riwayat", "transaksi", "published_date")

class pustakawanserializer(serializers.ModelSerializer):
    # pustakawan = serializers.priarykeyrelatedfield(many=True, read_only=True)
    class Meta:
        model = pustakawan
        fields = ("id", "peminjam", "pengembalian", "pembelian", "nama_buku", "published_date")

class bukuserializer(serializers.ModelSerializer):
    class Meta:
        model = buku
        fields = ("id", "jumlah_buku", "jenis_buku", "penerbit", "published_date")