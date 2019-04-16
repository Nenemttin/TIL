from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class MagazineArticle(TitleDescriptionModel, TimeStampedModel):
    content = models.TextField()


# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Writer(TimeStamp):
    name = models.CharField(max_length=100, default='')


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, default='', unique=True)
    description = models.TextField(default='')


class Chapter(TitleDescriptionModel, TimeStampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=20)


class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)


class Reply(models.Model):
    content = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

