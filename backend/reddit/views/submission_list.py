from rest_framework.generics import ListAPIView


from reddit.serializers.submissions import RedditSubmissionSerializer
from reddit.models import Submission

class SubmissionListView(ListAPIView):
    serializer_class = RedditSubmissionSerializer

    def get_queryset(self):
        return Submission.objects.order_by('created_at')
