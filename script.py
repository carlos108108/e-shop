
from datetime import datetime
from datetime import date
from time import sleep
import re


class Item:
    def __init__(self, name, price, age_limit=0):
        self.name = name
        self.price = price
        self.age_limit = age_limit

    def is_allowed(self, customer_age):
        return customer_age >= self.age_limit


class Basket:
    def __init__(self):
        self.__items = list()
        self.discount = 0

    @property
    def total_price(self):
        return round(sum(map(lambda x: x.price, self.__items)) * (1 - self.discount), 2)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount

    def add(self, item):
        self.__items.append(item)

    def remove(self, item):
        self.__items.remove(item)


class Customer:
    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.basket = Basket()
        self.email = Email
        self.password = Password

        if self.birthdate.strftime('%m %d') == date.today().strftime('%m %d'):
            print('today is your B-day so you\'ve got a special discount 10% more')
            self.basket._discount = .1

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, new_basket):
        self._basket = new_basket

    @property
    def age(self):
        return round((date.today() - self.birthdate).days / 365, 2)

    def add_to_basket(self, item):
        if isinstance(item, Item):
            if item.is_allowed(self.age):
                self._basket.add(item)
            else:
                print(f'you have to be older then {item.age_limit}')
        else:
            print(f'{item} is not in our offer')

    def remove_from_basket(self, item):
        if isinstance(item, Item):
            self._basket.remove(item)
        else:
            print(f'{item} is not in your basket')


class PremiumCustomer(Customer):
    discount_plan = {'bronze': .09, 'silver': .12, 'gold': .15, 'platinum': .21, 'VIP': .23}

    def __init__(self, admitted_discount='bronze', **kwargs):
        super().__init__(**kwargs)
        self.admitted_discount = admitted_discount

    def get_discount(self):
        if self.admitted_discount in PremiumCustomer.discount_plan:
            self.basket.discount += PremiumCustomer.discount_plan[self.admitted_discount]
            print(f'price after your {self.admitted_discount} discount: {self.basket.total_price}')
            return self.basket.discount
        else:
            raise AttributeError(f'admitted_discount has to be in range {list(PremiumCustomer.discount_plan)}')


class EmployeeCustomer(PremiumCustomer):
    def __init__(self, performance=0, **kwargs):
        super().__init__(**kwargs)
        self.performance = performance
        self.admitted_discount = self.value_of_performance()

    def value_of_performance(self):
        if self.performance > 90:
            self.admitted_discount = 'gold'
        elif self.performance > 80:
            self.admitted_discount = 'silver'
        return self.admitted_discount


class Manager(EmployeeCustomer):
    def __init__(self, admitted_discount='platinum', **kwargs):
        super().__init__(**kwargs)
        self.admitted_discount = admitted_discount

    def change_performance(self, surname, performance, value):
        setattr(surname, performance, value)

class Email:
    def __init__(self):
        self.email = input('enter your username (email): ')

    def __str__(self):
        return f'{self.email}'

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if re.search('@', new_email):
            self._email = new_email
        else:
            raise AttributeError(f'choose the email better')


class Password:
    def __init__(self):
        self.password = input('enter password: ')

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, new_password):
        res = self.verify_password(new_password)
        if res == 'password ok':
            self.__password = new_password
            print('password ok')
        else:
            print(f'{res}, choose the password better')


    @password.deleter
    def password(self):
        raise AttributeError('cannot delete password')

    def verify_password(self, password):
        x = None
        if len(password) < 8:
            x = 'too short'
        elif not re.search('[A-Z]', password):
            x = 'capitals missing'
        elif not re.search('[a-z]', password):
            x = 'lower missing'
        elif not re.search('[\x21-\x2F]', password):
            x = 'ASCII missing'
        elif not re.search('\d', password):
            x = 'digits missing'
        return x if x else 'password ok'


# john = PremiumCustomer(name='john', surname='smith', birthdate=date(2000, 4, 20))
# john.email()
# john.password()

# bread = Item('bread', 3)
# butter = Item('butter', 10)
# wine = Item('wine', 21, 18)

# mary = Manager(name='john', surname='smith', birthdate=date(2000, 4, 20))
# print(john.performance)
# mary.change_performance(john, 'performance', 91)
# print(john.performance)
# john.value_of_performance()
# #john.get_discount()
# #print(john.performance)
# john.add_to_basket(bread)
# print(john.basket.total_price)
# john.add_to_basket(butter)
# print(john.basket.total_price)
# john.add_to_basket(wine)
# print(john.basket.total_price)
# john.get_discount()
# print(john.basket.total_price)
# #print(john.performance)
# #john.get_discount = 'silver'
# print(john.basket.total_price)
# mary.add_to_basket(bread)
# print(mary.basket.total_price)
# mary.get_discount()
# print(mary.basket.total_price)

