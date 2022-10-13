# Generated by Django 2.2.9 on 2022-10-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20221013_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Book Chapters', 'Book Chapters'), ('Books', 'Books'), ('Journal', 'Journal'), ('International Reports', 'International Reports')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Invited Talks', 'Invited Talks'), ('Conference Presentation', 'Conference Presentation'), ('Editorial Boards', 'Editorial Boards')], default='Invited Talks', max_length=60),
        ),
    ]