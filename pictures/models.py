from django.db.models import *

# Create your models here.

# d = (
#     (1, 'jsahfdkl'),
#     (2, 'skjdfhgkljhs'),
#     (3, 'sdkjfglksjd'),
# )
# e = (
#     ('a', 'slkdjhgladskj'),
#     ('b', 'dsjfhgkljsh')
# )
#
# class B(Model):
#     pass
#
# class A(Model):
#     a = CharField(verbose_name='Колонка 1', max_length=100, blank=True, null=True, db_index=True)
#     b = IntegerField('Колонка 2', default=1)
#     c = BooleanField('Колонка 3', default=True)
#     d = FloatField('Колонка 4')
#     e = ForeignKey(B, verbose_name='Колонка 3', null=True, default=1) #ссылка на таблицу B
#     f = ForeignKey('C', verbose_name='Колонка 4')
#     h = IntegerField('Колонка 5', choices=d)
#     i = CharField('Колонка 6', choices=e, max_length=1)
#
#
# class C(Model):
#     pass
#
#
# class F(Model):
#     pass
#
# class G(F):
#     pass

class Picture(Model):
    Name = CharField(verbose_name='Название картинки', max_length=250, db_index=True)
    Cost = FloatField('Цена')
    Placement = ForeignKey('Picture', verbose_name='Место')
    Year = IntegerField('год', default=1)
    Status = IntegerField('Статус', choices=Status, default=1)
