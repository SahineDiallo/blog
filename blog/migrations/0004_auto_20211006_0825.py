# Generated by Django 3.2.4 on 2021-10-06 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]