# Generated by Django 3.2.6 on 2023-02-26 16:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=5),
        ),
    ]