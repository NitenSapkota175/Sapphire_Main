# Generated by Django 3.2.14 on 2022-09-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sapphire', '0005_auto_20220829_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brochurepage',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]