from .models import User


#
#
def user_id_validation(user_id):
    user = User.objects.filter(user_id=float(user_id)).first()
    print(user)
    return user
#
#
# def user_name_validation(user_name):
#     if len(User.objects.filter(name=user_name)) > 0:
#         return True
#     return False
