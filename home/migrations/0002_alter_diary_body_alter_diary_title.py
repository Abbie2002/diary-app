# Generated by Django 4.0.2 on 2022-02-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='body',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
