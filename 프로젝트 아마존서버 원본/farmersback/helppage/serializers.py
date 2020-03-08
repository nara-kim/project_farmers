from rest_framework import serializers
from .models import HelpModel

class HelpSerializers(serializers.ModelSerializer):
    class Meta:
        model = HelpModel
        fields = ['id', 'user', 'help_select', 'title','location1','location2', 'help_date','people','content', 'username']