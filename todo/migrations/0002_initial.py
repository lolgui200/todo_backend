# Generated by Django 4.1.7 on 2023-04-15 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomPrenom', models.CharField(max_length=255)),
                ('Puce', models.CharField(max_length=255)),
                ('sexe', models.CharField(choices=[('hongre', 'hongre'), ('étalon', 'étalon'), ('jument', 'jument')], max_length=10)),
                ('poney', models.BooleanField()),
                ('UELN', models.CharField(max_length=255)),
                ('DTN', models.CharField(max_length=255)),
                ('IMA', models.CharField(max_length=50)),
                ('Note', models.CharField(max_length=255)),
                ('NomProp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.todouserprofile')),
            ],
        ),
    ]
