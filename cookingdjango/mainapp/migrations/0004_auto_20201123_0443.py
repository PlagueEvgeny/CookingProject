# Generated by Django 2.2 on 2020-11-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_subjectcategory_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='document',
            field=models.FileField(null=True, upload_to='media/book/'),
        ),
        migrations.AddField(
            model_name='books',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]