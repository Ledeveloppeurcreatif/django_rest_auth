from rest_framework import serializers
from backend.models import Categorie, Mission


class MissionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='titre'  
    )
    class Meta:
        model = Mission
        fields = '__all__'

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Categorie
        fields = '__all__'


# class SignalementSerializer(serializers.HyperlinkedModelSerializer):
#created_by = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = Signalement
#         fields = '__all__'