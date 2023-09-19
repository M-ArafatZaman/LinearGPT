from rest_framework import serializers

class ChatSerializer(serializers.ListSerializer):
    '''
    Serializer Class for the Chat Model that returns a list
    of chat owned by the user
    '''
    class Meta:
        pass