from rest_framework import generics, status
from rest_framework.response import Response
from .models import Question, Submission
from .serializers import QuestionSerializer, SubmissionSerializer
import random

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        question_type = self.request.query_params.get('type')
        if question_type:
            return self.queryset.filter(type=question_type)
        return self.queryset

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SubmissionCreateView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        question = serializer.validated_data['question']
        if question.type == 'SST':
            score = random.randint(0, 10)
        elif question.type == 'RO':
            score = self.calculate_ro_score(question, serializer.validated_data['user_answer'])
        elif question.type == 'RMMCQ':
            score = self.calculate_rmmcq_score(question, serializer.validated_data['user_answer'])
        serializer.save(score=score)

    def calculate_ro_score(self, question, user_answer):
        correct_order = [para.id for para in question.paragraphs.all()]
        user_order = list(map(int, user_answer.split(',')))
        score = sum([1 for i, para_id in enumerate(user_order) if para_id == correct_order[i]])
        return score


    def calculate_rmmcq_score(self, question, user_answer):
        correct_options = [option.id for option in question.options.filter(is_correct=True)]
        user_selected_options = list(map(int, user_answer.split(',')))
        correct_selections = len(set(user_selected_options) & set(correct_options))
        incorrect_selections = len(set(user_selected_options) - set(correct_options))
        if incorrect_selections > 0:
            score = max(correct_selections - incorrect_selections, 0)
        else:
            score = correct_selections

        return score


class PracticeHistoryView(generics.ListAPIView):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        question_type = self.request.query_params.get('type')
        queryset = Submission.objects.all()
        if question_type:
            queryset = queryset.filter(question__type=question_type)
        return queryset
