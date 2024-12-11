from django.db.models.signals import post_save
from django.dispatch import receiver
from v1.accounts.models.user import User
from v1.carts.models.cart import Cart
from v1.user_roles.models.customer import Customer


@receiver(post_save, sender=User)
def create_cart_for_customer(sender, instance, created, **kwargs):
    if created and instance.type_choice == 4:
        customer, customer_created = Customer.objects.get_or_create(user=instance)
        cart, cart_created = Cart.objects.get_or_create(user=customer)
