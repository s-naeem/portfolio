# Generated by Django 2.0.2 on 2018-09-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_about_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='button_text',
            field=models.CharField(blank=True, default='Know More', max_length=255, null=True),
        ),
    ]
