# Generated by Django 3.1.5 on 2021-02-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizzaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzatype', models.CharField(choices=[('R', 'Regular'), ('S', 'Square')], max_length=20)),
                ('pizzasize', models.CharField(max_length=20)),
                ('pizzatopping', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Pizza_Info',
            },
        ),
    ]
