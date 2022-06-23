from rest_framework import serializers

from testapp.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['name', 'file']
