from django.forms import ModelForm, Textarea, TextInput
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
       labels = {'name': 'имя', 'lang': 'язык', 'code': 'код'}
       widgets = {
          'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
          'code': TextInput(attrs={'placeholder': 'Код сниппета'}),
       }

class SnippetdelForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name']
       labels = {'name': 'Введите имя'}
       widgets = {
          'name': TextInput(attrs={'placeholder': 'для удаления'}),
       }