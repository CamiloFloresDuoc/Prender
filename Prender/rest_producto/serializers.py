from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nom_prod', 'desc_prod', 'valor_prod', 'cantidad', 'user', 'categoria']