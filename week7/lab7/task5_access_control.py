# task5_access_control.py

from functools import wraps
# Global login status
is_logged_in = True
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in first.")
            return None
    return wrapper
@require_login
def view_account():
    print("Welcome to your account!")
    print("You can now view your account details.")
# Case 1: User is logged in
print("When is_logged_in = True:")
is_logged_in = True
view_account()
# Case 2: User is not logged in
print("\nWhen is_logged_in = False:")
is_logged_in = False
view_account()

'''output:
When is_logged_in = True:
Welcome to your account!
You can now view your account details.

When is_logged_in = False:
Access denied. Please log in first.'''
