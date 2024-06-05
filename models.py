from django.db import models


# Create your models here.
class buku(models.Model):
    jumlah_buku = models.CharField(max_length=100)
    jenis_buku = models.TextField()
    penerbit = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.jumlah_buku

class peminjam(models.Model):
    nama_peminjam = models.CharField(max_length=100)
    riwayat = models.TextField()
    transaksi = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_peminjam

class pustakawan(models.Model):
    peminjam = models.ForeignKey(peminjam, related_name='pustakawan', on_delete=models.CASCADE)
    pengembalian = models.CharField(max_length=100)
    pembelian = models.TextField()
    nama_buku = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.peminjam

