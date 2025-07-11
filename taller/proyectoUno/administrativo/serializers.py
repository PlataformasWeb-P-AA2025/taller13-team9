from django.contrib.auth.models import User, Group
from administrativo.models import Edificio, Departamento

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = '__all__'


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    edificio = serializers.HyperlinkedRelatedField(
        queryset=Edificio.objects.all(),
        view_name='edificio-detail'
    )

    class Meta:
        model = Departamento
        fields = '__all__'
