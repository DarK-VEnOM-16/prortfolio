# Generated by Django 2.2.9 on 2022-08-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('university', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info', models.TextField()),
                ('category', models.CharField(choices=[('Journal', 'Journal'), ('Articles', 'Articles'), ('International Reports', 'International Reports')], default='Journal', max_length=60)),
                ('date', models.DateField(null=True)),
                ('associated_contact', models.ManyToManyField(blank=True, related_name='users', to='portfolio.Users')),
            ],
        ),
    ]