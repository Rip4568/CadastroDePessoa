# Generated by Django 4.0.5 on 2022-06-21 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoa_app', '0003_alter_contato_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contato', to='Pessoa_app.pessoa'),
        ),
    ]
