# Generated by Django 4.1.2 on 2022-12-29 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.ForeignKey(default='', max_length=100, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]