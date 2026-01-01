from rest_framework import serializers

class HousePredictionSerializer(serializers.Serializer):
    area = serializers.FloatField()
    bedrooms = serializers.IntegerField()
