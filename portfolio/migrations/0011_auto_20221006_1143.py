# Generated by Django 3.2.9 on 2022-10-06 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20221006_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Books', 'Books'), ('Journal', 'Journal'), ('Book Chapters', 'Book Chapters'), ('Conference', 'Conference'), ('International Reports', 'International Reports')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Editorial Boards', 'Editorial Boards'), ('Invited Talks', 'Invited Talks'), ('Conference Presentation', 'Conference Presentation')], default='Invited Talks', max_length=60),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(choices=[('Alumini', 'Alumini'), ('Team', 'Team')], default='Team', max_length=60),
        ),
    ]