# Generated by Django 2.2.4 on 2020-03-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0085_auto_20200228_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='payout_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=50, null=True),
        ),
    ]