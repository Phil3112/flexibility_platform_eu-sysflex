# Generated by Django 2.0.7 on 2020-05-05 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0005_flexibilityactivationconfirmation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flexibilityactivationorder',
            old_name='forwarded_quantity',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='flexibilityactivationconfirmation',
            name='flexibility_activation_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='activation.FlexibilityActivationOrder'),
            preserve_default=False,
        ),
    ]