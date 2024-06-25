from tkinter import *

# window
my_window = Tk()
my_window.title("ماشین پخت مستر پخت")
my_window.geometry("400x300")
# calculator_screen
result = StringVar()
Label(my_window, text="به نام خدا ", font=("Arial", 20)).place(x=148, y=20)
Label(my_window, text="ماشین پخت مستر پخت ", font=("Arial", 14)).place(x=248, y=60)
Label(my_window, text="ماشین پخت سارنده دستگاه تمام اتوماتیک لواش (روتاری) ",
      font=("Arial", 14)).place(x=40, y=90)
Label(my_window, text="به مدیریت : دلیری", font=("Arial", 14)).place(x=270, y=120)
Label(my_window, text="شماره تماس : 09126115113", font=("Arial", 14)).place(x=180, y=150)
Label(my_window, text="نشانی : شهریار چهارراه ملارد خیابان کشاورز جنب ",
      font=("Arial", 14)).place(x=70, y=180)
Label(my_window, text="سوپر مارکت",
      font=("Arial", 14)).place(x=300, y=205)


def employee_click(self):
    self.my_window.destroy()


# btn_customer
btn_customer = Button(my_window, text="پنل مشتریان", width=10, height=1)
btn_customer.place(x=20, y=240)
# btn_employee
btn_employee = Button(self.my_window, text="پنل کارکنان", font=("Arial Black", 20), width=10,
                      height=1, command=self.employee_click)
btn_employee.place(x=110, y=240)
# btn_device
btn_device = Button(my_window, text="دستگاه ها", width=10, height=1)
btn_device.place(x=200, y=240)
# btn_3
btn_component = Button(my_window, text="قطعات", width=10, height=1)
btn_component.place(x=290, y=240)

my_window.mainloop()
