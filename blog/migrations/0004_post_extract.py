# Generated by Django 4.2.16 on 2024-11-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='extract',
            field=models.TextField(blank=True),
        ),
    ]