import bcrypt

class PasswordHandler:

    def encrypt_password(self, password: str):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed_password
    
    def check_password(self, password: str, hashed_password):

        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

