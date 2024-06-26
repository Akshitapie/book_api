# Generated by Django 3.2.5 on 2024-06-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='page',
            field=models.IntegerField(default='NULL'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default='NULL'),
        ),
    ]
