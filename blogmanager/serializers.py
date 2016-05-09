from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

    class Meta:

        """ meta datas of model
        """
        model = Blog
        fields = (
            'name',
            'title',
            'description'
            )
