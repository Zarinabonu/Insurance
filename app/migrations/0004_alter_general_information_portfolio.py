# Generated by Django 3.2.5 on 2021-08-03 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_portfolio_contract_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_information',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.portfolio'),
        ),
    ]
