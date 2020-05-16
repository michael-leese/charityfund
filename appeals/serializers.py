from rest_framework import serializers
from appeals.models import Appeal
"""
used to serialize our data to pass to Map API call
"""
class AppealsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        model = Appeal
        fields = ('id', 'title', 'latitude', 'longitude')