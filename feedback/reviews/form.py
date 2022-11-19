from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=50, error_messages={
#         "max_length": "Please use shorter name!",
#         "required": "This field cannot be empty!"
#     })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # to create form for every parameter in the model class
        fields = '__all__'
        # exclude = ["owner_comment"] # to exclude something that we do not want in the form field from model
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "max_length": "Please use shorter name!",
                "required": "This field cannot be empty!"
            }


        }
