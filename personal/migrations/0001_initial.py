# Generated by Django 2.2.24 on 2021-07-06 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.TextField()),
                ('image_path', models.ImageField(upload_to='pictures/')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Location')),
            ],
        ),
    ]
