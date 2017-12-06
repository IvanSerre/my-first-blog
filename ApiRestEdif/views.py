from ApiRestEdif.models import Residente,D
from ApiRestEdif.serializers import ResidenteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ListResidentes(APIView):
    model = Residente
    def get(self, request, format=None):
        residente = Residente.objects.all()
        serializer = ResidenteSerializer(residente, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        residente = ResidenteSerializer(data=request.data)
        if residente.is_valid():
            residente.save()
            return Response(residente.data, status=status.HTTP_201_CREATED)

        return Response(residente.errors, status=status.HTTP_400_BAD_REQUEST)
