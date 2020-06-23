# Generated by Django 2.2.10 on 2020-06-22 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200622_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubOrder',
            fields=[
                ('sub_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Sub')),
                ('quantity', models.IntegerField(default=1)),
            ],
            bases=('orders.sub',),
        ),
    ]