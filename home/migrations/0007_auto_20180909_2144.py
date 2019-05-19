# Generated by Django 2.0.2 on 2018-09-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180909_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='cv',
            field=models.FileField(blank=True, default='About/NID-card.pdf', upload_to='About/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='sub_title',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, default='about me', max_length=25, null=True),
        ),
    ]