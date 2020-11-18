# Generated by Django 3.1.3 on 2020-11-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('avtor', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True)),
                ('pages', models.IntegerField(default=0)),
                ('format', models.CharField(choices=[('a', 'Аудио формат'), ('t', 'Бумажный формат'), ('el', 'Электронный формат')], default='a', max_length=2)),
                ('industries', models.CharField(choices=[('w', 'Военная история'), ('c', 'История культуры'), ('s', 'История науки'), ('r', 'История государства и права '), ('p', 'История политических и правовых учений'), ('re', 'История религии'), ('e', 'История экономики')], default='w', max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subjectcategory')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]