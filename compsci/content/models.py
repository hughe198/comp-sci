from django.db import models
from django.conf import settings
from accounts.models import NewUser


# Create your models here.

class HomePageTopPost(models.Model):
    title = models.TextField()
    message = models.TextField()
    link = models.URLField(blank = True)
    create_at = models.DateTimeField(auto_now = True)
    upload = models.ImageField(upload_to ='static/content/', blank = False)
    Bg_Colour = models.TextField()

class GalleryImage(models.Model):
    image = models.ImageField(upload_to ='content/', blank = False)
    caption = models.TextField( blank = True, null =True)


class BaseHelpers(models.Model):
    image = models.ImageField(upload_to ='static/question/', blank = True, null =True)
    class Meta:
        abstract = True


class Answer(BaseHelpers):
    question= models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
    )
    topic= models.ForeignKey(
        'Topic',
        on_delete=models.CASCADE,
    )
    question_set= models.ForeignKey(
        'QuestionSet',
        on_delete=models.CASCADE,
    )
    correct = models.BooleanField(default=False)
    answer = models.TextField(default ="")
    def __str__(self):
        return self.answer

class Topic(models.Model):
    qual_name = models.TextField(default ="GCSE")
    unit_name = models.TextField(default ="Unit 1")
    topic_name = models.TextField()
    image = models.ImageField(upload_to ='static/content/', blank = True)
    def __str__(self):
        return self.unit_name +" "+ self.topic_name


class Question(BaseHelpers):
    topic= models.ForeignKey(
        'Topic',
        on_delete=models.CASCADE,
    )
    question_set= models.ForeignKey(
        'QuestionSet',
        on_delete=models.CASCADE,
    )
    question = models.TextField(default ="")
    def __str__(self):
        return self.question

    def get_answers(self):
        return self.answer_set.all()

class QuestionSet(models.Model):
    quiz_name = models.TextField(default ="Quiz")
    topic= models.ForeignKey(
        'Topic',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.quiz_name

    def get_questions(self):
        return self.question_set.all()


class Tags(models.Model):
    questionset = models.ForeignKey(
        QuestionSet,
        on_delete=models.CASCADE,
        null =True, blank = True)

    tag = models.TextField(null = True,blank = True)
    def __str__(self):
        return self.tag

class UserProfile(models.Model):
    user = models.OneToOneField(NewUser, null = True, on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='static/content/profiles', blank = True)
    teacher = models.BooleanField(default=False)
    # def __str__(self):
    #     return self.user.email

class User_Question_Answer(models.Model):
    user = models.OneToOneField(NewUser, null = True, on_delete = models.CASCADE)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        )
    answer= models.ForeignKey(Answer, on_delete = models.CASCADE)
