from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.medicion.models import Medicion
from apps.medicion.api.serializers import (
        MedicionSerializer,
        MedicionSaveSerializer,
        MedicionMaxSerializer, 
        MedicionMinSerializer, 
        MedicionAvgSerializer
    )
from django.db.models import (
        Max, 
        Min, 
        Avg
    )


@api_view(['GET', 'POST'])
def medicion_api_view(request):

    # List
    if request.method == 'GET':
        medicion = Medicion.objects.all()
        medicion_serializer = MedicionSerializer(medicion, many = True)
        return Response(medicion_serializer.data, status = status.HTTP_200_OK)

    #  Create
    elif request.method == 'POST':
        
        values = []
        all_values = request.data['sensor_data']
        
        for value in all_values:
            sensor_data = {"sensor_data" : value}
            values.append(sensor_data)

        medicion_serializer = MedicionSaveSerializer(data=values, many=True)

        # Validation
        if medicion_serializer.is_valid():
            medicion_serializer.save()
            return Response({"success":"true"}, status = status.HTTP_201_CREATED)

        return Response(medicion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def max_view(request):

    # Max
    if request.method == 'GET':
        maximo = Medicion.objects.all().aggregate(max=Max('sensor_data'))
        max_serializer = MedicionMaxSerializer(maximo)
        return Response(max_serializer.data, status = status.HTTP_200_OK)



@api_view(['GET'])
def min_view(request):

    # Min
    if request.method == 'GET':
        minimo = Medicion.objects.all().aggregate(min=Min('sensor_data'))
        min_serializer = MedicionMinSerializer(minimo)
        return Response(min_serializer.data, status = status.HTTP_200_OK)



@api_view(['GET'])
def avg_view(request):

    # Avg
    if request.method == 'GET':
        promedio = Medicion.objects.all().aggregate(avg=Avg('sensor_data'))
        avg_serializer = MedicionAvgSerializer(promedio)
        return Response(avg_serializer.data, status = status.HTTP_200_OK)
