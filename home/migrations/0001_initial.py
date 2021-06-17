# Generated by Django 3.2.2 on 2021-05-10 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('household', models.CharField(default='what is the name of your pastor', max_length=500)),
                ('redemmed', models.CharField(default='what is the name of your pastor', max_length=500)),
                ('mountain', models.CharField(default='what is the name of your pastor', max_length=500)),
                ('christ', models.CharField(default='what is the name of your pastor', max_length=500)),
                ('apostolic', models.CharField(default='what is the name of your pastor', max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=500)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question')),
            ],
        ),
    ]