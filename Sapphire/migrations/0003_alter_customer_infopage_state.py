# Generated by Django 3.2.14 on 2022-08-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sapphire', '0002_brochurepage_customer_infopage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_infopage',
            name='State',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
