from django.db.models.signals import post_save
from django.dispatch import receiver
from v1.accounts.models.user import User
from v1.user_roles.models.customer import Customer


@receiver(post_save, sender=User)
def create_customer_for_user_type_4(sender, instance, created, **kwargs):
    if created and instance.type_choice == 4:
        Customer.objects.get_or_create(user=instance)
