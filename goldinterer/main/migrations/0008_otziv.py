# Generated by Django 4.0.4 on 2022-12-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tovar_interyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otziv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('comment', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
