import random
from django.conf import settings
from django.utils import timezone


from datetime import timedelta
from uuid import uuid4

# from users.models import Notification


EMAIL_ADMIN = settings.DEFAULT_FROM_EMAIL
D = "deposit"
W = "withdraw"

ADMIN_ADDRESS = {
    "BTC": "18gTvDGzJKW9N1ovMh6pL77d7eGDRnHnCj",
    "ETH": "0xF3f2136F6e34CB413e3887B978fD3015a1EECC4a",
    "USDT": "0xF3f2136F6e34CB413e3887B978fD3015a1EECC4a",
}
wallets = ["BTC", "ETH", "USDT"]


def gen_random_number():
    return str(random.randint(100000, 999999))


# def set_expirable_var(session, var_name, value, expire_at):
#     session[var_name] = {'value': value, 'expire_at': expire_at.timestamp()}

# def get_expirable_var(session, var_name, default=None):
#     var = default
#     if var_name in session:
#         my_variable_dict = session.get(var_name, {})
#         if my_variable_dict.get('expire_at', 0) > datetime.now().timestamp():
#             var = my_variable_dict.get('value')
#         else:
#             del session[var_name]
#     return var


# def verify_exp():
#     return timezone.now() + timedelta(minutes=10)


def reg_code():
    code = str(uuid4()).replace(" ", "-").upper()[:6]
    return code


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_next_destination(request):
    next = None
    if request.GET.get("next"):
        next = str(request.GET.get("next"))
    return next


def get_deadline(h):
    return timezone.now() + timedelta(hours=h)


def earnings(amount, perc):
    p = (perc / 100) * amount
    return p + amount


def create_notification(**info):
    """
    Create A New notification Object
    """
    notification = info["model"](
        user=info["user"], title=info["title"], body=info["body"]
    )
    notification.save()
    return notification


def trans_code():
    code = str(uuid4()).replace(" ", "-").upper()[:8]
    return code


def check_user(email, model):
    account = None
    try:
        account = model.objects.get(email__exact=email)
    except model.DoesNotExist:
        account = None

    return account


def check_user_address(user):
    if user.btc_address and user.eth_address and user.usdt_address:
        return True
    else:
        return False


def get_user_address(user, method):
    address = None
    if method == "BTC":
        address = user.btc_address
    elif method == "ETH":
        address = user.eth_address
    elif method == "USDT":
        address = user.usdt_address
    else:
        address = None

    return address
