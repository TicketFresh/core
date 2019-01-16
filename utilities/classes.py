import uuid
import datetime


class user:
    def __init__(self, first_name, last_name, status):
        #TODO: add phone number, address company etc.
        self.first_name = first_name
        self.last_name = last_name
        self.status = status

    def __str__(self):
        values = "\nFirst Name: {} \nLast Name: {} \nStatus: {}".format(self.first_name, self.last_name, self.status)
        return values

    def __repr__(self):
        values = "\nFirst Name: {} \nLast Name: {} \nStatus: {}".format(self.first_name, self.last_name, self.status)
        return values

class company:
    def __init__(self, name):
        #TODO: add phone number, email, point of contact etc.
        self.name = name


class ticket:
    def __init__(self, title, client_name, company_name, last_update, status):
        #TODO: Add more things
        self.id = uuid.uuid4()
        self.title = title
        self.client_name = client_name
        self.company_name = company_name
        self.last_update = last_update
        self.status = status
    
    def __str__(self):
        values = "\nID: {} \nTitle: {} \nClient Name: {} \nCompany Name: {} \nLast Update: {} \nStatus: {}".format(
            self.id,
            self.title,
            self.client_name,
            self.company_name,
            self.last_update,
            self.status
        )
        return values
    
    def __repr__(self):
        values = "\nID: {} \nTitle: {} \nClient Name: {} \nCompany Name: {} \nLast Update: {} \nStatus: {}".format(
            self.id,
            self.title,
            self.client_name,
            self.company_name,
            self.last_update,
            self.status
        )
        return values

class inventory_item:
    def __init__(self):
        pass

class customer:
    def __init__(self):
        self.asset = asset
        pass

class invoice:
    def __init__(self):
        pass

class message:
    def __init__(self):
        pass