# Generated by Django 2.2.1 on 2019-06-01 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pill_detection', '0006_pillinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='pillinformation',
            name='char',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
