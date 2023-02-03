from django import forms
from app.models import *
class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)


class ModelTopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class ModelWebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['topic_name','url']
        #widgets={'name':forms.PasswordInput}
        #labels={'topic_name':'TN','name':'NA'}
        #help_texts={'topic_name':'should not be instegers','name':'only alphabates'}

class ModelaccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
                #fields=['name']
        #exclude=['url']
        #widgets={'name':forms.PasswordInput}
        #labels={'name':'NA'}
        #help_texts={'name':'only alphabates'}

