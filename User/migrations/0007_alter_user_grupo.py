# Generated by Django 4.0.4 on 2022-05-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_user_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grupo',
            field=models.CharField(choices=[('EQUIPE', 'EQUIPE'), ('FCB', 'FCB'), ('GALERIA', 'GALERIA'), ('DPZT', 'DPZT')], max_length=50, null=True),
        ),
    ]