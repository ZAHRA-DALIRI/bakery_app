import re
from datetime import date

from model.entity import *


class Employee(Base):
    __tablename__ = "employee_tbl"
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _national_code = Column("national_code", String(10), unique=True, nullable=False)
    _phone_number = Column("phone_number", String(20), nullable=False)
    _email = Column("email", String(50), nullable=False)
    _address = Column("address", String(40), nullable=False)
    _birth_certificate_number = Column("birth_certificate_number", String(20), unique=True, nullable=False)
    _birth_date = Column("birth_date", Date, nullable=False)
    _field_of_study = Column("field_of_study", String(50), nullable=False)
    _grade = Column("grade", String(20), nullable=False)
    _average = Column("average", String(10), nullable=False)
    _start_date = Column("start_date", Date, nullable=False)
    _completion_date = Column("completion_date", Date, nullable=False)
    _university_name = Column("university_name", String(50), nullable=False)
    _status = Column("status", Boolean, default=True)

    sells = relationship("Sell", back_populates="employee")

    def __init__(self, name, family, national_code, phone_number, email, address,
                 birth_certificate_number, birth_date, field_of_study, grade, average, start_date,
                 completion_date, university_name, status=True):
        self.employee_id = None
        self.name = name
        self.family = family
        self.national_code = national_code
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.birth_certificate_number = birth_certificate_number
        self.birth_date = birth_date
        self.field_of_study = field_of_study
        self.grade = grade
        self.average = average
        self.start_date = start_date
        self.completion_date = completion_date
        self.university_name = university_name
        self.status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[A-Za-zآ-ی_\-\s]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام نامعتبر است")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if re.match(r"^[A-Za-zآ-ی_\-\s]+$", family, re.I):
            self._family = family
        else:
            raise ValueError(" فامیلی نامعتبر است")

    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, national_code):
        if re.match(r"^[\d{3}_\d{7}\s]+$", national_code):
            self._national_code = national_code
        else:
            raise ValueError("کد ملی نامعتبر است")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if re.match(r"^[\d\s-]+$", phone_number):
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
        if re.match(r"^[\w\sآ-ی]+$", address, re.I):
            self._address = address
        else:
            raise ValueError("آدرس نامعتبر است ")

    @property
    def birth_certificate_number(self):
        return self._birth_certificate_number

    @birth_certificate_number.setter
    def birth_certificate_number(self, birth_certificate_number):
        if re.match(r"^[\w\sآ-ی]+$", birth_certificate_number, re.I):
            self._birth_certificate_number = birth_certificate_number
        else:
            raise ValueError("شماره شناسنامه نامعتبر است")

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
    def field_of_study(self):
        return self._field_of_study

    @field_of_study.setter
    def field_of_study(self, field_of_study):
        if re.match(r"^[\w\sآ-ی]+$", field_of_study, re.I):
            self._field_of_study = field_of_study
        else:
            raise ValueError("رشته ی تحصیلی نامعتبر است")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if re.match(r"^[\w\sآ-ی]+$", grade, re.I):
            self._grade = grade
        else:
            raise ValueError("مقطع تحصیلی نامعتبر است")

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, average):
        if re.match(r"^[\w\sآ-ی.]+$", average, re.I):
            self._average = average
        else:
            raise (ValueError("معدل نامعتبر است"))

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, date):
            self._start_date = start_date
        else:
            raise (ValueError("تاریخ شروع نامعتبر است"))

    @property
    def completion_date(self):
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        if isinstance(completion_date, date):
            self._completion_date = completion_date
        else:
            raise (ValueError("تاریخ اتمام نامعتبر است"))

    @property
    def university_name(self):
        return self._university_name

    @university_name.setter
    def university_name(self, university_name):
        if re.match(r"^[\w\sآ-ی]+$", university_name, re.I):
            self._university_name = university_name
        else:
            raise ValueError("نام دانشگاه نامعتبر است")
