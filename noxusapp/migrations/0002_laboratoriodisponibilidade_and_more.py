# Generated by Django 5.0.4 on 2024-04-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noxusapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratorioDisponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.IntegerField()),
                ('diaSemana', models.IntegerField()),
                ('horaInicio', models.TimeField()),
                ('horaTermino', models.TimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='laboratorios',
            old_name='nomeLoboratorio',
            new_name='nomeLaboratorio',
        ),
        migrations.AlterField(
            model_name='laboratorios',
            name='descricao',
            field=models.CharField(max_length=1000),
        ),
    ]
