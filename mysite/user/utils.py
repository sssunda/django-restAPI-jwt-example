
def jwt_payload_handler(token, user, request):
    return {
        'token' : token,
        'user' : user.username,
        'password' : user.password
    }   