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
    (1, 'New'),
)


class Artist(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    about = CharField(max_length=1000)
    country = ForeignKey('Country', verbose_name='Страна', null=True, blank=True, db_index=True, on_delete=SET_NULL)
    date_of_birth = DateField('Дата рождения', null=True, blank=True)
    date_of_death = DateField('Дата смерти', null=True, blank=True)


class Gallery(Model):
    name = CharField(max_length=100)
    pictures = CharField(max_length=1000)
    phone = CharField(max_length=12)
    address = CharField(max_length=100)


class Genre(Model):
    name = CharField(max_length=100)


class Placement(Model):
    name = CharField(verbose_name='Название', max_length=250)
    address = CharField(verbose_name='Адрес', max_length=250, db_index=True)


class Department(Placement):
    phone = CharField(max_length=12)
    gallery = ForeignKey(Gallery, verbose_name='Галерея', db_index=True, on_delete=CASCADE)


class Country(Model):
    name = CharField(verbose_name='Страна', max_length=300)


class Expo(Placement):
    opening_time = DateField('Дата открытия', null=False, auto_now=False)
    closing_time = DateField('Дата закрытия', null=False, auto_now=False)


class Employee(Model):
    name = CharField(verbose_name='ФИО сотрудника', max_length=100, blank=False, null=False, db_index=True)
    telephone = CharField(verbose_name='Телефон', max_length=15, blank=False, null=False, db_index=True)
    position = CharField(verbose_name='Позиция', max_length=100, blank=False, null=False, db_index=True)
    department = ForeignKey(Department, verbose_name='Отдел', null=True, on_delete=SET_NULL)


class Journal(Model):
    picture = ForeignKey('Picture', verbose_name='Картина', db_index=True, on_delete=CASCADE)
    date = DateField(verbose_name='Дата', max_length=100, blank=False, null=False, db_index=True)
    employee = ForeignKey(Employee, verbose_name='Сотрудник', blank=True, null=True, on_delete=SET_NULL)
    placement_from = ForeignKey(Placement, verbose_name='Откуда', related_name='placement_from', on_delete=CASCADE)
    placement_to = ForeignKey(Placement, verbose_name='Куда', related_name='placement_to', on_delete=CASCADE)


class Picture(Model):
    name = CharField(verbose_name='Название', max_length=250, db_index=True)
    author =  ForeignKey(Artist, verbose_name='Автор', null=True, on_delete=SET_NULL)
    cost = FloatField('Цена')
    placement = ForeignKey(Placement, verbose_name='Место', null=True, on_delete=SET_NULL)
    year = IntegerField('год', default=1)
    status = IntegerField('Статус', choices=Status, default=1)
    gallery = ForeignKey(Gallery, verbose_name='Галерея',db_index=True, on_delete=CASCADE)
