# Generated by Django 2.2.2 on 2020-05-02 14:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotes', '0007_auto_20200502_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='thumbup',
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbup',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]