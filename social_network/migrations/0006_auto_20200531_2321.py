# Generated by Django 3.0.6 on 2020-05-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0005_auto_20200530_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('activity_date', models.DateTimeField(auto_now=True)),
                ('endpoint', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='likeunlike',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
