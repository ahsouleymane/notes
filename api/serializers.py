from rest_framework.serializers import ModelSerializer
from .Model import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        field = '__all__'