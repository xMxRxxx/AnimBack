from rest_framework import serializers
from .models import njItem,njSubItem


class NjSubItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = njSubItem
        fields = "__all__"
class NjItemSerializer(serializers.ModelSerializer):
    itemanime = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = njItem
        fields = "__all__"
# class NjItemTopSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = njTopRecom
#         fields = ('id' ,'title','title1', 'title2')

