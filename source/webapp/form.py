from django import forms

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class BookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label="Автор")
    email = forms.EmailField(max_length=50, required=True, label="Мэйл")
    description = forms.CharField(max_length=100, required=True, label="Описание")

