import re
from datetime import date

from model.entity import *


class Customer(Base):
    __tablename__ = "customer_tbl"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _national_code = Column("national_code", String(15), unique=True, nullable=False)
    _phone_number = Column("phone_number", String(20), nullable=False)
    _email = Column("email", String(80), nullable=False)
    _address = Column("address", String(150), nullable=False)
    _birth_date = Column("birth_date", Date, nullable=True)
    _user_name = Column("user_name", String(30), nullable=False)
    _password = Column("password", String(30), nullable=False)
    _status = Column("status", Boolean, default=True)

    sells = relationship("Sell", back_populates="customer")

    def __init__(self, name, family, national_code, phone_number, email, address,
                 birth_date, user_name, password, status=True):
        self.customer_id = None
        self.name = name
        self.family = family
        self.national_code = national_code
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.birth_date = birth_date
        self.user_name = user_name
        self.password = password
        self.status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[A-Za-zآ-ی_\-\s.]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام نامعتبر است")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if re.match(r"^[A-Za-zآ-ی_\-\s.]+$", family, re.I):
            self._family = family
        else:
            raise ValueError(" فامیلی نامعتبر است")

    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, national_code):
        if re.match(r"^[-\d_\s]+$", national_code):
            self._national_code = national_code
        else:
            raise ValueError("کد ملی نامعتبر است")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if re.match(r"^[-._\d+\s]+$", phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError("شماره تلفن نامعتبر است")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email, re.I):
            self._email = email
        else:
            raise ValueError("ایمیل نامعتبر است")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if re.match(r"^[-.،()?؟!{}+,\w\sآ-ی]+$", address, re.I):
            self._address = address
        else:
            raise ValueError("آدرس نامعتبر است ")

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        if isinstance(birth_date, date):
            self._birth_date = birth_date
        else:
            raise ValueError("تاریخ تولد نامعتبر است")

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        if re.match(r"^[-.@#*!$%^&\w\sآ-ی]+$", user_name, re.I):
            self.user_name = user_name
        else:
            raise ValueError("نام کاربری نامعتبر است")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if re.match(r"^[-.@#*!$%^&\w\sآ-ی]+$", password, re.I):
            self.password = password
        else:
            raise ValueError("کلمه عبور نامعتبر است")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, bool):
            self._status = status
        else:
            raise ValueError("وضعیت نامعتبر است")
