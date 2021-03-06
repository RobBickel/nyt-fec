# Generated by Django 2.0.1 on 2018-07-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_2018', '0029_auto_20180724_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='filing',
            name='computed_ie_total_for_f24',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="computed total IEs for F24s for alerting so we know if they're big enough to care about", max_digits=12, null=True),
        ),
    ]
