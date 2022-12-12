from django.urls import path

from .views.submission_list import SubmissionListView

urlpatterns = [
    path('submissions/', SubmissionListView.as_view(), name="submission_list"),
]
