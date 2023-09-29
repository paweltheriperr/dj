from rest_framework import serializers
from .models import Fen

class FenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fen
        fields = '__all__'
