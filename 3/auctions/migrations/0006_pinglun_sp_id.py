# Generated by Django 4.0.3 on 2022-04-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_shangpin_sp_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinglun',
            name='sp_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]