from admin_UI.models import Faculty, Specialty, Group, Subject, Rating, Student
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SubjectInfoSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class PostBinSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return PostBin.objects.create(**validated_data)

    def update(self, instace, validated_data):
        instace.title = validated_data.get('title', instace.title)
        instace.text = validated_data.get('text', instace.text)
        instace.save()
        return instace
