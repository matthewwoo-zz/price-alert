import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @classmethod
    def get_by_email(cls, email):
        pass

    @staticmethod
    def is_login_valid(email, password):
        user_data = Database.find_one("users", {"email": email}) # Password is in sha512 -> pbdkf2_sha512
        if user_data is None:
            raise UserErrors.UserNotExistsError("Your user does not exist.")

        if not Utils.check_hashed_password(password,user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True

        # """
        # This method verifies that an e-mail/password combo (as sent by the site forms) is valid or not.
        # Checks that the e-mail exists, and that the password associated to that e-mail is correct.
        # :param email: The user's email
        # :param password: A sha512 hashed password
        # :return: True if valid, False otherwise
        # """

    @staticmethod
    def register_user(email, password):
        user_data = Database.find_one("users", {"email": email})

        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError("The e-mail you used to register already exists.")
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The e-mail does not have the right format.")

        User(email, Utils.hash_password(password)).save_to_db()
        return True

    def save_to_db(self):
        Database.insert("users", self.json())


    def json(self):
        return {"_id": self._id,
                "email": self.email,
                "password": self.password
        }

