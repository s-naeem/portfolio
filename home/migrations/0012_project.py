# Generated by Django 2.0.2 on 2018-09-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20180909_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, default='Threads', max_length=50, null=True)),
                ('category', models.CharField(blank=True, default='Illustration', max_length=50, null=True)),
                ('thumb_1', models.ImageField(blank=True, upload_to='Portfolio/%Y/%m/%d')),
                ('thumb_2', models.ImageField(blank=True, upload_to='Portfolio/%Y/%m/%d')),
                ('project_info', models.TextField(blank=True, null=True)),
                ('clients', models.CharField(blank=True, default='Brand & Co.', max_length=50, null='True')),
                ('tools', models.CharField(blank=True, max_length=255, null=True)),
                ('live_url', models.URLField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]