from rest_framework import serializers
from reddit.models import Submission

class RedditSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
