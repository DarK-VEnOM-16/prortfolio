# Generated by Django 3.2.9 on 2022-10-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20220924_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map_Locations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=600)),
                ('lat', models.CharField(max_length=60)),
                ('lng', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Book Chapters', 'Book Chapters'), ('Journal', 'Journal'), ('International Reports', 'International Reports'), ('Books', 'Books'), ('Conference', 'Conference')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Invited Talks', 'Invited Talks'), ('Editorial Boards', 'Editorial Boards'), ('Conference Presentation', 'Conference Presentation')], default='Invited Talks', max_length=60),
        ),
    ]
