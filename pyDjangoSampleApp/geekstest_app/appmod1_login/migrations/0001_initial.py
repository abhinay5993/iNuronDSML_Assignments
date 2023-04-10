# Generated by Django 4.1.7 on 2023-04-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lstName', models.CharField(max_length=50)),
                ('ageVal', models.IntegerField(default=0, null=True)),
                ('emailVal', models.EmailField(max_length=254)),
                ('genderVal', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
            ],
        ),
    ]
