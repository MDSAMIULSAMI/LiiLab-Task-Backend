from django.db import models

class QuestionType(models.Model):
    name = models.CharField(max_length=255)

class Question(models.Model):
    QUESTION_TYPES = [
        ('SST', 'Summarize Spoken Text'),
        ('RO', 'Re-Order Paragraph'),
        ('RMMCQ', 'Reading Multiple Choice (Multiple)'),
    ]
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=5, choices=QUESTION_TYPES)

class Audio(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='audios')
    speaker = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audios/')

class Paragraph(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='paragraphs')
    text = models.TextField()

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.TextField()
    score = models.IntegerField()
    submission_date = models.DateTimeField(auto_now_add=True)
