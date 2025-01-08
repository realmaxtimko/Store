from rest_framework import serializers
from female.models import WomensClothing

class WomanClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomensClothing
        fields = "__all__"