# Generated by Django 2.0.4 on 2018-04-14 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('vote_taken', models.DateTimeField(default=django.utils.timezone.now)),
                ('ayes', models.IntegerField()),
                ('nays', models.IntegerField()),
            ],
        ),
    ]
