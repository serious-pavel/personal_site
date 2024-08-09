
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_author", "comment_content",]
        labels = {
            "comment_author": "Your Name",
            "comment_content": "Your Comment",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }
