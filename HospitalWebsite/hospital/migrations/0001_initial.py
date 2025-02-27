# Generated by Django 4.1.7 on 2023-02-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700)),
                ('feature_image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('department', models.CharField(choices=[('Heart Center', 'Heart Center'), ('Neuroscience Center', 'Neuroscience Center'), ('Obesity Center', 'Obesity Center'), ('Eye Center', 'Eye Center'), ('Orthopedic Center', 'Orthopedic Center'), ('Pediatric Center', 'Pediatric Center')], max_length=1000)),
                ('established_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
