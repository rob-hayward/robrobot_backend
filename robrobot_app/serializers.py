# robrobot_app/serializers.py
from rest_framework import serializers
from .models import Profile, Project, GitRepository, ProjectImage, Technology


class GitRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GitRepository
        fields = ['url', 'name']


class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name', 'icon']


class ProjectSerializer(serializers.ModelSerializer):
    git_repo_links = GitRepositorySerializer(many=True, read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    technologies_used = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'