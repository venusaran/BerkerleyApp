from rest_framework import serializers


class CountSerializer(serializers.Serializer):
    visit_count = serializers.IntegerField()

    class Meta:
        fields = ['visit_count']


class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()

    class Meta:
        fields = ['error']
