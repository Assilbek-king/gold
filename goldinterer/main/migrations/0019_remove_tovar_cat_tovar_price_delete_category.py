# Generated by Django 4.0.4 on 2023-02-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_delete_partner_remove_tovar_img1_remove_tovar_img2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='cat',
        ),
        migrations.AddField(
            model_name='tovar',
            name='price',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]