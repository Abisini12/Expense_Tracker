# Generated by Django 5.0 on 2024-01-03 19:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseTracker', '0002_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='cpassword',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=5, message='Ensure this field has at least 5 characters.')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=8, message='Ensure this field has at least 8 characters.')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=10, message='Ensure this field has at least 10 characters.')]),
        ),
    ]
