# Generated by Django 4.0.2 on 2022-03-01 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('account_creation', models.DateField(auto_now=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('user_gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Non binary/None of these choices')], max_length=32, null=True)),
                ('user_age', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=300, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
