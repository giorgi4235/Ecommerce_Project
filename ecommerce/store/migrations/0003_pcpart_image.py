# Generated by Django 5.1 on 2024-08-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcpart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
