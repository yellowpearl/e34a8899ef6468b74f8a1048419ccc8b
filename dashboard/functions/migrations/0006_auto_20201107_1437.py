# Generated by Django 3.1.3 on 2020-11-07 14:37

from django.db import migrations, models
import functions.models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0005_auto_20201107_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='img_alt',
            field=models.TextField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='function',
            name='img',
            field=models.ImageField(default='Error', upload_to=functions.models.Function.img_path),
        ),
    ]
