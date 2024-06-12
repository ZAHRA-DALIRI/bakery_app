import re
from datetime import date

from model.entity import *


class Component(Base):
    __tablename__ = "component_tbl"
    component_id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(50), nullable=False)
    _model = Column("model", String(50), nullable=False)
    _serial = Column("serial", String(100), nullable=False)
    _description = Column("description", String(300), nullable=False)
    _production_date = Column("production_date", Date, nullable=False)

    device_id = Column(Integer, ForeignKey("device_tbl.device_id"))
    device = relationship("Device")

    def __init__(self, name, model, serial, description, production_date, device):
        self.component_id = None
        self.name = name
        self.model = model
        self.serial = serial
        self.description = description
        self.production_date = production_date
        self.device = device

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[A-Za-zآ-ی_\-\s.]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام قطعه نامعتبر است ")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if re.match(r"^[,-.\w\sآ-ی]+$", model, re.I):
            self._model = model
        else:
            raise ValueError("مدل قطعه نامعتبر است")

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, serial):
        if re.match(r"^[,-.\w\sآ-ی]+$", serial):
            self._serial = serial
        else:
            raise ValueError("سریال قطعه نامعتبر است")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if re.match(r"^[-.,،()\w\sآ-ی]+$", description, re.I):
            self._description = description
        else:
            raise ValueError("توضیحات قطعه نامعتبر است ")

    @property
    def production_date(self):
        return self._production_date

    @production_date.setter
    def production_date(self, production_date):
        if isinstance(production_date, date):
            self._production_date = production_date
        else:
            raise ValueError("تاریخ تولید نامعتبر است")
