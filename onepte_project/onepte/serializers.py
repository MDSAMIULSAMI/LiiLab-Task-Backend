from rest_framework import serializers
from .models import Question, Audio, Paragraph, Option, Submission

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['speaker', 'audio_file']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['text']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    audios = AudioSerializer(many=True, read_only=True)
    paragraphs = ParagraphSerializer(many=True, read_only=True)
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'type', 'audios', 'paragraphs', 'options']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['question', 'user_answer', 'score', 'submission_date']
