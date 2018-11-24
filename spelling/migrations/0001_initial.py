# Generated by Django 2.1.3 on 2018-11-20 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='ngram',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spelling.Word'),
        ),
    ]