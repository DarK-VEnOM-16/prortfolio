# Generated by Django 3.2.9 on 2022-10-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(blank=True, max_length=3000, null=True)),
                ('url', models.CharField(blank=True, max_length=3000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(max_length=3000)),
                ('subject', models.CharField(max_length=3000)),
                ('affilation', models.CharField(max_length=3000)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Map_Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=600)),
                ('lat', models.CharField(max_length=60)),
                ('lng', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(blank=True, max_length=3000, null=True)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info', models.TextField()),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info', models.TextField()),
                ('category', models.CharField(choices=[('Journal', 'Journal'), ('International Reports', 'International Reports'), ('Books', 'Books'), ('Conference', 'Conference'), ('Book Chapters', 'Book Chapters')], default='Journal', max_length=60)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reasearch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info', models.TextField()),
                ('category', models.CharField(choices=[('Conference Presentation', 'Conference Presentation'), ('Invited Talks', 'Invited Talks'), ('Editorial Boards', 'Editorial Boards')], default='Invited Talks', max_length=60)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(choices=[('Alumini', 'Alumini'), ('Team', 'Team')], default='Team', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='View_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
