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
    Name = models.CharField(verbose_name='ФИО сотрудника', max_length=100, blank=False, null=False, db_index=True)
    Telephone = models.CharField(verbose_name='Телефон', max_length=15, blank=False, null=False, db_index=True)
    Position = models.CharField(verbose_name='Позиция', max_length=100, blank=False, null=False, db_index=True)
    department = models.ForeignKey(Department)


class Position(Model):
    Position = (
        (1, 'Director'),
        (2, 'Manager'),
        (3, 'Resrorer'),
        (4, 'Admin')
    )


class Status (Model)
    Status = (
        (1, 'N')
    )


class Journal(Model):
    Picture = models.PictureField(verbose_name='Картина', max_length=100, blank=False, null=False, db_index=True)
    Date = models.DateField(verbose_name='Дата', max_length=100, blank=False, null=False, db_index=True)
    Employee = models.ForeignKey(Employee)
    Placement = models.ForeignKey(Placement)
    Placement = models.ForeignKey(Placement)
