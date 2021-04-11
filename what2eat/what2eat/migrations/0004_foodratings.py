# Generated by Django 3.1.7 on 2021-04-11 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('what2eat', '0003_auto_20210404_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('ratings', models.IntegerField(default=0)),
                ('foodid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='what2eat.food')),
            ],
        ),
    ]
