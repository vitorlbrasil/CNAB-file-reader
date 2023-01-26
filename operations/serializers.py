from rest_framework import serializers
from .models import Operation


class OperationSerializer(serializers.ModelSerializer):
    cnab_file = serializers.FileField(write_only=True)

    def create(self, validated_data):
        return Operation.objects.create(**validated_data)

    class Meta:
        model = Operation
        fields = [
            "id",
            "type",
            "date",
            "value",
            "cpf",
            "card",
            "hour",
            "store",
            "cnab_file",
        ]
        read_only_fields = [
            "id",
            "type",
            "date",
            "value",
            "cpf",
            "card",
            "hour",
            "store",
        ]
        depth = 1


class OperationFileSerializer(serializers.Serializer):
    ...
