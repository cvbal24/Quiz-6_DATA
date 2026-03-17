from django.db import migrations


def seed_subscription_tiers(apps, schema_editor):
    SubscriptionTier = apps.get_model('subscription', 'SubscriptionTier')

    default_tiers = [
        {'name': 'Bronze', 'price': '10.00', 'max_usage': 10},
        {'name': 'Silver', 'price': '20.00', 'max_usage': 25},
        {'name': 'Gold', 'price': '30.00', 'max_usage': 50},
    ]

    for tier in default_tiers:
        SubscriptionTier.objects.get_or_create(
            name=tier['name'],
            defaults={
                'price': tier['price'],
                'max_usage': tier['max_usage'],
            },
        )


def unseed_subscription_tiers(apps, schema_editor):
    SubscriptionTier = apps.get_model('subscription', 'SubscriptionTier')
    SubscriptionTier.objects.filter(name__in=['Bronze', 'Silver', 'Gold']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_subscription_tiers, unseed_subscription_tiers),
    ]