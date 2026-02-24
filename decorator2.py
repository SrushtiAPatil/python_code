def require_login(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access Denied!")
    return wrapper

@require_login
def dashboard(user):
    print("Welcome to dashboard")

dashboard("admin")
dashboard("guest")