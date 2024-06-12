class CustomerNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Customer not found")


class EmployeeNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Employee not found")


class DeviceNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Device not found")


class ComponentNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Component not found")


class DuplicateUsernameError(Exception):
    def __init__(self):
        Exception.__init__(self, "Duplicate username !!!")


class UsernameNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Username not found")


class PasswordNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Password not found")
