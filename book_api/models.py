from django.db import models

from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100, default="NULL")
    publish_date = models.DateField(default="2020-09-10", null=True)
    page = models.IntegerField(default="NULL")
    # cover_url = models.ImageField(upload_to="images/", default="default.jpg")
    cover_url = models.URLField(max_length=255, null=True)


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_get_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    fees = models.IntegerField(default=0)
