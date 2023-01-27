from rest_framework import serializers
from .models import Store
import ipdb


class StoreSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    def get_balance(self, obj):
        result = 0
        for operation in obj.operations.values("value"):
            result += operation["value"]
        return result

    class Meta:
        model = Store
        fields = [
            "id",
            "store_name",
            "store_owner",
            "balance",
            "operations",
        ]
        depth = 1
