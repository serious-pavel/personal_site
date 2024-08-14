
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_author", "comment_content",]
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }
        widgets = {
            "comment_author": forms.TextInput(attrs={
                # "class": "comment-author-input",
                "placeholder": "Your Name",
            }),
            "comment_content": forms.Textarea(attrs={
                # "class": "comment-content-input",
                "placeholder": "Your Comment",
            })
        }
