# Generated by Django 3.0.8 on 2020-09-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_auto_20200902_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='Email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Phone',
            field=models.CharField(default='0000000000', help_text='Enter you 10 digit mobile number', max_length=10),
        ),
    ]
