# Generated by Django 2.2.9 on 2022-09-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20220903_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='view_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Articles', 'Articles'), ('Journal', 'Journal'), ('International Reports', 'International Reports')], default='Journal', max_length=60),
        ),
    ]