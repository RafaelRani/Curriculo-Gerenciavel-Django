# Generated by Django 3.0.3 on 2020-02-22 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='hora',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='instituicao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='escolaridade',
            name='inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interesse',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
