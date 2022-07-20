from django.core.mail import send_mail


def sending_mail(situation, company, order_id, sender_email, recipient_email):

    if situation == "purchase":
        subject = f"{company}, {order_id} - purchase"
        message = "Thank you for your purchase in our shop."

    elif situation == "payment confirmation to consumer":
        subject = f"{company}, {order_id} - purchase"
        message = "Thank you for your payment."

    elif situation == "payment confirmation to merchant":
        subject = f"{order_id} - payment confirmation"
        message = f"Client has paid for order {order_id}. You can send the products"

    elif situation == "shipping confirmation":
        subject = f"{company}, {order_id} - shipping confirmation"
        message = "Good news. Your order is already sent"

    try:
        send_mail(subject, message, sender_email, recipient_email)
    except ValueError:
        pass
