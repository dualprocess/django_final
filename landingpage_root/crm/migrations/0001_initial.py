# Generated by Django 3.2.3 on 2021-05-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oder_dt', models.DateField(auto_now=True)),
                ('order_name', models.CharField(max_length=200)),
                ('order_phone', models.CharField(max_length=200)),
            ],
        ),
    ]
