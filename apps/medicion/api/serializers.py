from rest_framework import serializers
from apps.medicion.models import Medicion


class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['sensor_data']

    def to_representation(self,instance):
        if abs(instance.sensor_data) > abs(int(instance.sensor_data)):
            return {
                'sensor_data':instance.sensor_data
            }
        return {
            'sensor_data': int(instance.sensor_data)
        }


class MedicionSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['sensor_data']

    def create(self, validated_data):
        data = validated_data
        for sensor_data in data:
            Medicion.objects.create(**validated_data)
        return data


class MedicionMaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['sensor_data']

    def to_representation(self,instance):
        if abs(instance['max']) > abs(int(instance['max'])):
            return {
                'max':instance['max']
            }
        return {
            'max': int(instance['max'])
        }


class MedicionMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['sensor_data']

    def to_representation(self,instance):
        if abs(instance['min']) > abs(int(instance['min'])):
            return {
                'min':instance['min']
            }
        return {
            'min': int(instance['min'])
        }


class MedicionAvgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['sensor_data']

    def to_representation(self,instance):
        if abs(instance['avg']) > abs(int(instance['avg'])):
            return {
                'avg':instance['avg']
            }
        return {
            'avg': int(instance['avg'])
        }



# class MedicionAvgSerializer(serializers.Serializer):
#     avg = serializers.FloatField()

#     def to_representation(self,instance):
#         if abs(instance['avg']) > abs(int(instance['avg'])):
#             return {
#                 'avg':instance['avg']
#             }
#         return {
#                 'avg': int(instance['avg'])
#             }

    