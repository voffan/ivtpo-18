from django.forms import Form, CharField, PasswordInput, TextInput


class AuthForm(Form):
    login = CharField(label='Логин', max_length=100, widget=TextInput)
    pwd = CharField(label='Пароль', max_length=100, widget=PasswordInput)
