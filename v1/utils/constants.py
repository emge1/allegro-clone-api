ERROR = 'Error'
SUCCESS = 'Success'

# User types
USER_TYPE_CHOICES = (
    (1, "Administrator"),
    (2, "Staff"),
    (3, "Merchant"),
    (4, "Customer"),
)

# Permissions
PERMISSION_ADMINISTRATOR_REQUIRED = 'Administrator permissions needed'
PERMISSION_STAFF_REQUIRED = 'Staff permissions needed'
PERMISSION_MERCHANT_REQUIRED = 'Merchant permissions needed'
PERMISSION_CUSTOMER_REQUIRED = 'Customer permissions needed'


# User roles
USER_ROLE_ADMINISTRATOR = 'administrator'
USER_ROLE_STAFF = 'staff'
USER_ROLE_MERCHANT = 'merchant'
USER_ROLE_CUSTOMER = 'customer'

# Media types
MEDIA_TYPE_CHOICES = (
    (1, "Image"),
    (2, "Video"),
)

# Transaction types
TRANSACTION_TYPE_CHOICES = (
    (1, "Buy"),
    (2, "Sell"),
)