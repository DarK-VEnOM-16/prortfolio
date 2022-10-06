# Generated by Django 3.2.9 on 2022-10-06 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20221006_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Books', 'Books'), ('Book Chapters', 'Book Chapters'), ('International Reports', 'International Reports'), ('Journal', 'Journal')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Conference Presentation', 'Conference Presentation'), ('Invited Talks', 'Invited Talks'), ('Editorial Boards', 'Editorial Boards')], default='Invited Talks', max_length=60),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(choices=[('Team', 'Team'), ('Alumini', 'Alumini')], default='Team', max_length=60),
        ),
    ]