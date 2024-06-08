import re

from model.entity import *


class Sell(Base):
    __tablename__ = "sell_tbl"
    sell_id = Column(Integer, primary_key=True, autoincrement=True)
    date_time = Column(DateTime)
    price = Column(Integer)

    device_id = Column(Integer, ForeignKey("device_tbl.device_id"))
    device = relationship("Device")

    customer_id = Column(Integer, ForeignKey("customer_tbl.customer_id"))
    customer = relationship("Customer")

    emp_id = Column(Integer, ForeignKey("employee_tbl.employee_id"))
    employee = relationship("Employee")

    def __init__(self, date_time, price, device, customer, employee):
        self.sell_id = None
        self.date_time = date_time
        self.price = price
        self.device = device
        self.customer = customer
        self.employee = employee

    # @property
    # def sell_id(self):
    #     return self._sell_id
    #
    # @sell_id.setter
    # def sell_id(self, sell_id):
    #     if isinstance(sell_id, int):
    #         self._sell_id = sell_id
    #     else:
    #         raise ValueError("شناسه فروش نامعتبر است")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if re.match("^[\w\sآ-ی]+$", price, re.I):
            self._price = price
        else:
            raise ValueError("مبلغ نامعتبر است")
