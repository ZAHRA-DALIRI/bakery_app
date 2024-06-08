import re

from model.entity import *


class Component(Base):
    __tablename__ = "component_tbl"
    component_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=False)
    serial = Column(String(20), nullable=False)
    description = Column(String(100))

    device_id = Column(Integer, ForeignKey("device_tbl.device_id"))
    device = relationship("Device")

    def __init__(self, name, model, serial, description, device):
        self.component_id = None
        self.name = name
        self.model = model
        self.serial = serial
        self.description = description
        self.device = device

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[\w\sآ-ی]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام قطعه نامعتبر است ")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if re.match(r"^[\w\sآ-ی]+$", model, re.I):
            self._model = model
        else:
            raise ValueError("مدل قطعه نامعتبر است")

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, serial):
        if re.match(r"^[0-9_ \s]+$", serial):
            self._serial = serial
        else:
            raise ValueError("سریال قطعه نامعتبر است")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if re.match(r"^[\w\sآ-ی]+$", description, re.I):
            self._description = description
        else:
            raise ValueError("توضیحات قطعه نامعتبر است ")
