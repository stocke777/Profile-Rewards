# Generated by Django 3.1.5 on 2021-03-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210305_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
