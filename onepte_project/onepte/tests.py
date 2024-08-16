from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Question

class QuestionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.question = Question.objects.create(title="Test Question", type="SST")

    def test_get_question_list(self):
        response = self.client.get(reverse('question-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_question_detail(self):
        response = self.client.get(reverse('question-detail', args=[self.question.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
