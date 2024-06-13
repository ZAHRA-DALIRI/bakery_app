from tkinter import *
import tkinter.messagebox as msg

from controller.customer_controller import CustomerController
from view import *


class CustomerView:
    def reset_form(self):
        self.customer_id.variable.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.national_code.variable.set("")
        self.phone_number.variable.set("")
        self.email.variable.set("")
        self.address.variable.set("")
        self.birth_date.variable.set("")
        self.user_name.variable.set("")
        self.password.variable.set("")
        self.status.variable.set("")
        status, customer_list = CustomerController.find_all()
        if status:
            self.table.refresh_table(customer_list)

    def select_row(self, customer):
        self.customer_id.variable.set(customer[0])
        self.name.variable.set(customer[1])
        self.family.variable.set(customer[2])
        self.national_code.variable.set(customer[3])
        self.phone_number.variable.set(customer[4])
        self.email.variable.set(customer[5])
        self.address.variable.set(customer[6])
        self.birth_date.variable.set(customer[7])
        self.user_name.variable.set(customer[8])
        self.password.variable.set(customer[9])
        self.status.variable.set(customer[10])

    def save_click(self):
        status, message = CustomerController.save(
            self.name.variable.get(),
            self.family.variable.get(),
            self.national_code.variable.get(),
            self.phone_number.variable.get(),
            self.email.variable.get(),
            self.address.variable.get(),
            self.birth_date.variable.get(),
            self.user_name.variable.get(),
            self.password.variable.get(),
            self.status.variable.get()
        )
        if status:
            msg.showinfo("ذخیره مشتری", "اطلاعات مشتری با موفقیت ذخیره شد")
            self.reset_form()
        else:
            msg.showerror("خطای ذخیره سازی", message)

    def edit_click(self):
        status, message = CustomerController.edit(
            self.customer_id.variable.get(),
            self.name.variable.get(),
            self.family.variable.get(),
            self.national_code.variable.get(),
            self.phone_number.variable.get(),
            self.email.variable.get(),
            self.address.variable.get(),
            self.birth_date.variable.get(),
            self.user_name.variable.get(),
            self.password.variable.get(),
            self.status.variable.get()
        )
        if status:
            msg.showinfo("ویرایش مشتری", "اطلاعات مشتری با موفقیت ویرایش شد ")
            self.reset_form()
        else:
            msg.showerror("خطای ویرایش", message)

    def remove_click(self):
        status, message = CustomerController.remove(self.customer_id.variable.get())
        if status:
            msg.showinfo("حدف مشتری", "اطلاعات مشتری با موفقیت حدف شد ")
            self.reset_form()
        else:
            msg.showerror("خطای حذف", message)

    def find_by_family(self, family):
        status, customer_list = CustomerController.find_by_family(self.search_family.variable.get())
        if status:
            self.table.refresh_table(customer_list)

    def close_form(self):
        main = MainView()

    def __init__(self):
        my_window = Tk()
        my_window.geometry("630x330")
        my_window.title("پروفایل مشتری")

        my_window.protocol("WM_DELETE_WINDOW", self.close_form)

        self.customer_id = TextWithLabel(my_window, "شناسه مشتری", 20, 20, disabled=True)
        self.name = TextWithLabel(my_window, "نام", 20, 60)
        self.family = TextWithLabel(my_window, "نام خانوادگی", 20, 100)
        self.national_code = TextWithLabel(my_window, "کد ملی", 20, 140)
        self.phone_number = TextWithLabel(my_window, "شماره تلفن", 20, 180)
        self.email = TextWithLabel(my_window, "ایمیل", 20, 120)
        self.address = TextWithLabel(my_window, "آدرس", 20, 160)
        self.birth_date = TextWithLabel(my_window, "تاریخ تولد", 20, 200)
        self.user_name = TextWithLabel(my_window, "نام کاربری", 20, 240)
        self.password = TextWithLabel(my_window, "رمز عبور", 20, 280)
        self.status = TextWithLabel(my_window, "وضعیت", 20, 320)
        self.search_family = TextWithLabel(my_window, "Search Family", 300, 360, distance=100)
        self.search_family.text_box.bind("<KeyRelease>", self.find_by_family)

        self.table = Table(my_window,
                           ["Id", "Name", "Family", "Username"],
                           [60, 100, 100, 100],
                           250,
                           20,
                           self.select_row)

        Button(my_window, text="Add", width=7, command=self.save_click).place(x=20, y=280)
        Button(my_window, text="Edit", width=7, command=self.edit_click).place(x=95, y=280)
        Button(my_window, text="Remove", width=7, command=self.remove_click).place(x=170, y=280)

        self.reset_form()

        my_window.mainloop()
