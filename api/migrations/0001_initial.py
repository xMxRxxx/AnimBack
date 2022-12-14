# Generated by Django 3.2.5 on 2022-07-31 23:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='njItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backdrop_path', models.ImageField(blank=True, null=True, upload_to='api/backdrop')),
                ('poster_path', models.ImageField(blank=True, null=True, upload_to='api/poster')),
                ('series', models.CharField(blank=True, max_length=1000, null=True)),
                ('category', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=512, null=True), default=[''], size=None)),
                ('description', models.TextField(blank=True, null=True)),
                ('episode', models.CharField(blank=True, max_length=1000, null=True)),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=512, null=True), default=[''], size=None)),
                ('producers', models.CharField(blank=True, max_length=1000, null=True)),
                ('rate', models.FloatField(blank=True, default=0, null=True)),
                ('release', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
                ('trailer_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='njSubItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('upload_at', models.DateField(blank=True, null=True)),
                ('link_360', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=512, null=True), default=[''], size=None)),
                ('link_480', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=512, null=True), default=[''], size=None)),
                ('link_720', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=512, null=True), default=[''], size=None)),
                ('link_1080', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=512, null=True), default=[''], size=None)),
                ('stream_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=1000, null=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemanime', to='api.njitem')),
            ],
        ),
    ]
