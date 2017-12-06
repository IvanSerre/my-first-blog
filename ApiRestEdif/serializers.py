from .models import Residente
from rest_framework import serializers
from datetime import datetime

class ResidenteSerializer(serializers.Serializer):
    rut = serializers.IntegerField()
    nombre = serializers.CharField()
    apellidomaterno = serializers.CharField()
    apellidopaterno = serializers.CharField()
    tipo = serializers.ChoiceField(choices=Residente.TIPO_RESIDENTE)
    created_date = serializers.DateTimeField()
    fechavigencia = serializers.DateTimeField()

    def create(self, validated_data):
        return Residente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rut = validated_data.get('rut', instance.rut)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellidomaterno = validated_data.get('apellidomaterno', instance.apellidomaterno)
        instance.apellidopaterno = validated_data.get('apellidopaterno', instance.apellidopaterno)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.fechavigencia = validated_data.get('fechavigencia', instance.fechavigencia)
        instance.save()
        return instance

"""
class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residente
        fields = ('rut', 'nombre', 'apellidomaterno', 'apellidopaterno', 'tipo', 'created_date', 'fechavigencia',)
"""
