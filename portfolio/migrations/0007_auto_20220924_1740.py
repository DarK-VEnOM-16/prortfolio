# Generated by Django 2.2.9 on 2022-09-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20220924_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Books', 'Books'), ('Journal', 'Journal'), ('Conference', 'Conference'), ('Book Chapters', 'Book Chapters'), ('International Reports', 'International Reports')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Invited Talks', 'Invited Talks'), ('Conference Presentation', 'Conference Presentation'), ('Editorial Boards', 'Editorial Boards')], default='Invited Talks', max_length=60),
        ),
    ]
