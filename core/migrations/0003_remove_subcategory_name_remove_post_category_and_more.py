# Generated by Django 4.1.2 on 2022-12-31 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
