from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'team_name', 'category', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '例：DOMについて'}),
            'team_name': forms.TextInput(attrs={'placeholder': '例：A'}),
            'category': forms.TextInput(attrs={'placeholder': '例：フロントエンド'}),
            'content': forms.Textarea(attrs={'placeholder': '質問内容を入力してください'}),
        }