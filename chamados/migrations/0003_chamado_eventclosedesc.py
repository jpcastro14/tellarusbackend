# Generated by Django 5.0.6 on 2025-02-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0002_chamado_eventcriticalitycolor_chamado_eventtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='eventCloseDesc',
            field=models.CharField(default='Teste', max_length=2000),
            preserve_default=False,
        ),
    ]
