import re

from model.entity import *


class Device(Base):
    __tablename__ = "device_tbl"
    device_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=False)

    components = relationship("Component", back_populates="device")

    def __init__(self, name, model):
        self.device_id = None
        self.name = name
        self.model = model

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[\w\sآ-ی]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام دستگاه نامعتبر است ")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if re.match(r"^[\w\sآ-ی]+$", model, re.I):
            self._model = model
        else:
            raise ValueError("مدل دستگاه نامعتبر است")
