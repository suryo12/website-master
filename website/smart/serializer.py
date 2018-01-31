from rest_framework import serializers

from .models import NodeID, Data

class NodeIDSerializer(serializers.ModelSerializer):
	class Meta:
		model = Data
		fields = '__all__'