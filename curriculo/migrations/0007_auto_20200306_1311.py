# Generated by Django 3.0.3 on 2020-03-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0006_auto_20200306_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complementar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sobre',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sobre',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sobre',
            name='nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
