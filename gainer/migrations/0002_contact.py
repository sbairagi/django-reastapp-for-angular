# Generated by Django 3.0.4 on 2020-03-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]