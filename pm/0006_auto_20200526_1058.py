# Generated by Django 2.2.6 on 2020-05-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pancar', '0005_auto_20200421_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='process',
            name='category',
            field=models.ManyToManyField(related_name='processes', to='pancar.Category'),
        ),
    ]
