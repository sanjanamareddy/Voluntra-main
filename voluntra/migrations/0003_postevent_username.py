# Generated by Django 4.0.10 on 2023-11-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntra', '0002_postevent_minage'),
    ]

    operations = [
        migrations.AddField(
            model_name='postevent',
            name='username',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
    ]
