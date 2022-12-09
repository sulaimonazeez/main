# Generated by Django 4.1.3 on 2022-12-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='myapp/static')),
                ('date', models.DateTimeField(auto_now=True)),
                ('describtion', models.TextField()),
            ],
        ),
    ]
