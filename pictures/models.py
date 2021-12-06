from django.db.models import *

# Create your models here.
'''
d = (
    (1, 'jsahfdkl'),
    (2, 'skjdfhgkljhs'),
    (3, 'sdkjfglksjd'),
)
e = (
    ('a', 'slkdjhgladskj'),
    ('b', 'dsjfhgkljsh')
)

class B(Model):
    pass

class A(Model):
    a = CharField(verbose_name='Колонка 1', max_length=100, blank=True, null=True, db_index=True)
    b = IntegerField('Колонка 2', default=1)
    c = BooleanField('Колонка 3', default=True)
    d = FloatField('Колонка 4')
    e = ForeignKey(B, verbose_name='Колонка 3', null=True, default=1) #ссылка на таблицу B
    f = ForeignKey('C', verbose_name='Колонка 4')
    h = IntegerField('Колонка 5', choices=d)
    i = CharField('Колонка 6', choices=e, max_length=1)


class C(Model):
    pass


class F(Model):
    pass

class G(F):
    pass
'''

Position = (
    (1, 'Director'),
    (2, 'Manager'),
    (3, 'Resrorer'),
    (4, 'Admin')
)

Status = (
    (1, 'N')
)


class Artist(Model):
    a = CharField(max_length=30, help_text="Enter artist's name'")
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    about = CharField(max_length=1000)
    country = ForeignKey('Country', verbose_name='Страна', db_index=True)
    date_of_birth = DateField('Дата рождения', null=True, blank=True)
    date_of_death = DateField('Дата смерти', null=True, blank=True)


class Department(Model):
    name = CharField(max_length=100)
    phone = CharField(max_length=12)
    employee = ForeignKey('Employee', verbose_name='Сотрудник', db_index=True)
    placement = ForeignKey('Placement', verbose_name='Размещение', db_index=True)


class Gallery(Model):
    name = CharField(max_length=100)
    pictures = CharField(max_length=1000)
    phone = CharField(max_length=12)
    address = CharField(max_length=100)
    department = ForeignKey(Department, verbose_name='Отдел', db_index=True)
    picture = ForeignKey('Picture', verbose_name='Картина', db_index=True)


class Genre(Model):
    name = CharField(max_length=100)


class Placement(Model):
    Name = CharField(verbose_name='Название', max_length=250)
    address = CharField(verbose_name='Адрес', max_length=250, db_index=True)


class Country(Model):
    Name = CharField(verbose_name='Страна', max_length=300)


class Expo(Model):
    opening_time = DateField('Дата открытия', null=False, auto_now=False)
    closing_time = DateField('Дата закрытия', null=False, auto_now=False)
    Placement = ForeignKey('Placement', verbose_name='Адрес')


class Employee(Model):
    Name = CharField(verbose_name='ФИО сотрудника', max_length=100, blank=False, null=False, db_index=True)
    Telephone = CharField(verbose_name='Телефон', max_length=15, blank=False, null=False, db_index=True)
    Position = CharField(verbose_name='Позиция', max_length=100, blank=False, null=False, db_index=True)
    department = ForeignKey(Department)


class Journal(Model):
    Picture = ForeignKey('Picture', verbose_name='Картина', blank=False, null=False, db_index=True)
    Date = DateField(verbose_name='Дата', max_length=100, blank=False, null=False, db_index=True)
    Employee = ForeignKey(Employee)
    Placement = ForeignKey(Placement)
    Placement = ForeignKey(Placement)


class Picture(Model):
    Name = CharField(verbose_name='Название картинки', max_length=250, db_index=True)
    Cost = FloatField('Цена')
    Placement = ForeignKey('Picture', verbose_name='Место')
    Year = IntegerField('год', default=1)
    Status = IntegerField('Статус', choices='Status', default=1)