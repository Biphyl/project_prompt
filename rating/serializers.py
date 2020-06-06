from .models import Post,Profile
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title','image','description','link')
        
class ProfileSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (' first_name','last_name',' email',' bio',' profile_pic')