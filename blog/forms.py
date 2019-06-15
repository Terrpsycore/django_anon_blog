from django import forms


class NewPostForm(forms.Form):
    text = forms.CharField(label='Текст сообщения', max_length=5000)