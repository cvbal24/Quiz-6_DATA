# Generated manually for Order Phase 6 schema

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('users', '0002_customuser_auth_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_transaction_id', models.CharField(max_length=255, unique=True)),
                ('price_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_as_buyer', to='users.customuser')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='services.service')),
            ],
            options={
                'ordering': ['-date_purchased'],
            },
        ),
    ]
