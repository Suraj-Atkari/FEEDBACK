from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Review
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


# def review(request):
#     if request.method == "POST":

#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"])                  #as we use ModelForm this is not needed
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#     else:
#         form=ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

 # def get(self, request):
    #     return render(request, "reviews/thank_you.html")    #eliminated because of the TemplateView

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This is working!!"
        return context


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
# Above lines of code can be ignore if we used the bellow ListView
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review


class DetailReviewView(TemplateView):
    template_name = "reviews/detailed_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review
        return context
