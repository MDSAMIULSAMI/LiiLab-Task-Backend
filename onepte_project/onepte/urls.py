from django.urls import path
from .views import QuestionListView, QuestionDetailView, SubmissionCreateView, PracticeHistoryView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('submit/', SubmissionCreateView.as_view(), name='submission-create'),
    path('history/', PracticeHistoryView.as_view(), name='practice-history'),
]
