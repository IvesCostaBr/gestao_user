# Generated by Django 3.2 on 2021-04-12 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=12)),
                ('cidade', models.CharField(max_length=15)),
                ('pais', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=60)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=14)),
                ('profile_photo', models.FileField(blank=True, null=True, upload_to='profile/')),
                ('endereco', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_data.endereco')),
            ],
        ),
    ]
