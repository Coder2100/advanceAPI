from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


#Authentication & Permissions
from django.contrib.auth.models import User


#Hyperlinking our API, classes
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        #model = Snippet
       # fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
       model = User
       field = ('id', 'username', 'snippets')
"""
#creating user serializer
class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
       # owner = serializers.ReadOnlyField(source='owner.username')
      


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    linenos = serializers.BooleanField(required=False)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    #language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
"""

# more efficient way,  refactoring our serializer using the ModelSerializer

"""
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'style')

    def create(self, validated_data):
        #create and return snippet instance, given the validated data
        return Snippet.objects.create(**validated_data)
    def update(self, instance, validated_data):
        #update and return snippert instance given the validatd data
        instance.title = validated.get('title', instance.title)
        instance.code = validate_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.lanaguage)
        instance.style = validated_data.get('style', instance.style)
        instance.save()

        return instance

"""


    