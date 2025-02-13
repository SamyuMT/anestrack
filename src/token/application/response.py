class TokenResponse():

    @staticmethod
    def parsedToken(token_info):
        if token_info:
            return {
                "state": True
            }
        else:
            raise Exception("Usuario o contraseña incorrectos")