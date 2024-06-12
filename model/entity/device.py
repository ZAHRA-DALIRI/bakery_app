import re
from datetime import date

from model.entity import *


class Device(Base):
    __tablename__ = "device_tbl"
    device_id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(50), nullable=False)
    _model = Column("model", String(50), nullable=False)
    _production_date = Column("production_date", Date, nullable=False)

    components = relationship("Component", back_populates="device")

    def __init__(self, name, model, production_date):
        self.device_id = None
        self.name = name
        self.model = model
        self.production_date = production_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[A-Za-zآ-ی_\-\s.]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام دستگاه نامعتبر است ")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if re.match(r"^[,-.\w\s()آ-ی]+$", model, re.I):
            self._model = model
        else:
            raise ValueError("مدل دستگاه نامعتبر است")

    @property
    def production_date(self):
        return self._production_date

    @production_date.setter
    def production_date(self, production_date):
        if isinstance(production_date, date):
            self._production_date = production_date
        else:
            raise ValueError("تاریخ تولید نامعتبر است")
