from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=50, error_messages={
        "max_length": "Please use shorter name!",
        "required": "This field cannot be empty!"
    })
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
