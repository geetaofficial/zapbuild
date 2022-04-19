from rest_framework import serializers
from role.models import CustomUser
from tasks.models import Tasks

class UserSerializer(serializers.ModelSerializer):
    """User Model Serializer."""
    class Meta:
        model = CustomUser
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Task Model Serializer."""
    class Meta:
        model = Tasks
        fields = ('title', 'description', 'task_created', 'updated', 'status',)
    
    def validate(self, attrs):
        c_user = self.context['request'].user
        attrs['client_user'] = c_user

        return serializers.Serializer.validate(self, attrs)

class TaskAsignSerializer(serializers.ModelSerializer):
    """Task Model Serializer."""
    class Meta:
        model = Tasks
        fields = ('employee_user',)
        read_only_fields = ('title',)


class TaskStatusSerializer(serializers.ModelSerializer):
    """Task Model Serializer."""
    class Meta:
        model = Tasks
        fields = ('status',)
        read_only_fields = ('title',)



class TaskDistroySerializer(serializers.ModelSerializer):
    """Task Model Serializer."""
    class Meta:
        model = Tasks
        fields = ('status',)
        read_only_fields = ('title',)


