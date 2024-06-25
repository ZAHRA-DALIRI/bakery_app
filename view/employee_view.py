from tkinter import *
import tkinter.messagebox as msg

from controller.employee_controller import EmployeeController
from view import *


class EmployeeView:
    def reset_form(self):
        self.employee_id.variable.set("")
        self.name.variable.set("")
        self.family.variable.set("")
        self.national_code.variable.set("")
        self.phone_number.variable.set("")
        self.email.variable.set("")
        self.address.variable.set("")
        self.birth_certificate_number.variable.set("")
        self.birth_date.variable.set("")
        self.field_of_study.variable.set("")
        self.grade.variable.set("")
        self.average.variable.set("")
        self.start_date.variable.set("")
        self.completion_date.variable.set("")
        self.university_name.variable.set("")
        self.user_name.variable.set("")
        self.password.variable.set("")
        self.status.variable.set("")
        status, employee_list = EmployeeController.find_all()
        if status:
            self.table.refresh_table(employee_list)

    def select_row(self, employee):
        self.employee_id.variable.set(employee[0])
        self.name.variable.set(employee[1])
        self.family.variable.set(employee[2])
        self.national_code.variable.set(employee[3])
        self.phone_number.variable.set(employee[4])
        self.email.variable.set(employee[5])
        self.address.variable.set(employee[6])
        self.birth_certificate_number.variable.set(employee[7])
        self.birth_date.variable.set(employee[8])
        self.field_of_study.variable.set(employee[9])
        self.grade.variable.set(employee[10])
        self.average.variable.set(employee[11])
        self.start_date.variable.set(employee[12])
        self.completion_date.variable.set(employee[13])
        self.university_name.variable.set(employee[14])
        self.user_name.variable.set(employee[15])
        self.password.variable.set(employee[16])
        self.status.variable.set(employee[17])

    def save_click(self):
        status, message = EmployeeController.save(
            self.name.variable.get(),
            self.family.variable.get(),
            self.national_code.variable.get(),
            self.phone_number.variable.get(),
            self.email.variable.get(),
            self.address.variable.get(),
            self.birth_certificate_number.variable.get(),
            self.birth_date.variable.get(),
            self.field_of_study.variable.get(),
            self.grade.variable.get(),
            self.average.variable.get(),
            self.start_date.variable.get(),
            self.completion_date.variable.get(),
            self.university_name.variable.get(),
            self.user_name.variable.get(),
            self.password.variable.get(),
            self.status.variable.get()
        )
        if status:
            msg.showinfo("ذخیره کارمند", "اطلاعات کارمند با موفقیت ذخیره شد")
            self.reset_form()
        else:
            msg.showerror("خطای ذخیره سازی", message)

    def edit_click(self):
        status, message = EmployeeController.edit(
            self.employee_id.variable.get(),
            self.name.variable.get(),
            self.family.variable.get(),
            self.national_code.variable.get(),
            self.phone_number.variable.get(),
            self.email.variable.get(),
            self.address.variable.get(),
            self.birth_certificate_number.variable.get(),
            self.birth_date.variable.get(),
            self.field_of_study.variable.get(),
            self.grade.variable.get(),
            self.average.variable.get(),
            self.start_date.variable.get(),
            self.completion_date.variable.get(),
            self.university_name.variable.get(),
            self.user_name.variable.get(),
            self.password.variable.get(),
            self.status.variable.get()
        )
        if status:
            msg.showinfo("ویرایش کارمند", "اطلاعات کارمند با موفقیت ویرایش شد ")
            self.reset_form()
        else:
            msg.showerror("خطای ویرایش", message)

    def remove_click(self):
        status, message = EmployeeController.remove(self.employee_id.variable.get())
        if status:
            msg.showinfo("حدف کارمند", "اطلاعات کارمند با موفقیت حدف شد ")
            self.reset_form()
        else:
            msg.showerror("خطای حذف", message)

    def find_by_family(self, family):
        status, employee_list = EmployeeController.find_by_family(self.search_family.variable.get())
        if status:
            self.table.refresh_table(employee_list)

    def close_form(self):
        main = MainView()

    def __init__(self):
        win = Tk()
        win.geometry("1000x1000")
        win.title("پروفایل کارمند")

        win.protocol("WM_DELETE_WINDOW", self.close_form)

        self.employee_id = TextWithLabel(win, "شناسه کارمند", 20, 20, disabled=True)
        self.name = TextWithLabel(win, "نام", 20, 60)
        self.family = TextWithLabel(win, "نام خانوادگی", 20, 100)
        self.national_code = TextWithLabel(win, "کد ملی", 20, 140)
        self.phone_number = TextWithLabel(win, "شماره تلفن", 20, 180)
        self.email = TextWithLabel(win, "ایمیل", 20, 120)
        self.address = TextWithLabel(win, "آدرس", 20, 160)
        self.birth_certificate_number = TextWithLabel(win, "شماره شناسنامه", 20, 200)
        self.birth_date = TextWithLabel(win, "تاریخ تولد", 20, 240)
        self.field_of_study = TextWithLabel(win, "رشته تحصیلی", 20, 240)
        self.grade = TextWithLabel(win, "مقطع", 20, 280)
        self.average = TextWithLabel(win, "معدل", 20, 320)
        self.start_date = TextWithLabel(win, "تاریخ شروع", 20, 360)
        self.completion_date = TextWithLabel(win, "تاریخ اتمام", 20, 400)
        self.university_name = TextWithLabel(win, "نام دانشگاه", 20, 440)
        self.user_name = TextWithLabel(win, "نام کاربری", 20, 500)
        self.password = TextWithLabel(win, "رمز عبور", 20, 540)
        self.status = TextWithLabel(win, "وضعیت", 20, 600)
        self.search_family = TextWithLabel(win, "Search Family", 300, 640, distance=100)
        self.search_family.text_box.bind("<KeyRelease>", self.find_by_family)

        self.table = Table(win,
                           ["Id", "Name", "Family", "Username"],
                           [60, 100, 100, 100],
                           250,
                           20,
                           self.select_row)

        Button(win, text="Add", width=7, command=self.save_click).place(x=20, y=280)
        Button(win, text="Edit", width=7, command=self.edit_click).place(x=95, y=280)
        Button(win, text="Remove", width=7, command=self.remove_click).place(x=170, y=280)

        self.reset_form()

        win.mainloop()
