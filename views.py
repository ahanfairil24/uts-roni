from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import peminjam, buku, pustakawan
from .serializers import peminjamserializer, bukuserializer, pustakawanserializer
from rest_framework.views import APIView

class peminjamlistcreate(generics.ListCreateAPIView):
    queryset = peminjam.objects.all()
    serializer_class = peminjamserializer

    def delete(self, request, *args, **kwargs):
        peminjam.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class peminjamretrieveupdatedestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = peminjam.objects.all()
    serializer_class = peminjamserializer
    lookup_field = "pk"


class peminjamlist(APIView):
    def get(self, request, format=None):
        peminjam = peminjam.object.all()
        serializer = peminjamserializer(peminjam, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = peminjamserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class pustakawanlistcreate(generics.ListCreateAPIView):
    queryset = pustakawan.objects.all()
    serializer_class = pustakawanserializer

    def delete(self, request, *args, **kwargs):
        pustakawan.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class pustakawanretrieveupdatedestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = pustakawan.objects.all()
    serializer_class = pustakawanserializer
    lookup_field = "pk"

class bukulistcreate(generics.ListCreateAPIView):
    queryset = buku.objects.all()
    serializer_class = bukuserializer

    def delete(self, request, *args, **kwargs):
        buku.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class bukuretrieveupdatedestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = buku.objects.all()
    serializer_class = bukuserializer
    lookup_field = "pk"