class CredentialResponse():

    @staticmethod
    def parsedCredential(credential_info):
        if credential_info:
            return {
                "id": str(credential_info.get("_id")),
                "name":  credential_info.get("name"),
                "state": True
            }
        else:
            raise Exception("Usuario o contraseña incorrectos")