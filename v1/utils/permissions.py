from v1.user_roles.models.administrator import Administrator
from v1.user_roles.models.staff import Staff
from v1.user_roles.models.merchant import Merchant
from v1.user_roles.models.customer import Customer


def is_administrator(user):
    """
    Return true if user is administrator
    """

    if Administrator.objects.filter(user=user):
        return True
    return False


def is_staff(user):
    """
    Return true if user is moderator or higher
    """

    if Staff.objects.filter(user=user):
        return True
    return is_administrator(user)


def is_merchant(user):
    """
    Return true if user is merchant
    """

    if Merchant.objects.filter(user=user):
        return True
    return False


def is_customer(user):
    """
    Return true if user is customer
    """

    if Customer.objects.filter(user=user):
        return True
    return False
