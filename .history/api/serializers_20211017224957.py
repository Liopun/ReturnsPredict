from rest_framework import serializers

class ResponseSerializer(serializers.ModelSerializer):
    response = serializers.CharField()

    class Meta:
        fields = ['data']