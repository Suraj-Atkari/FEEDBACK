from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Review
from django.views.generic.edit import FormView, CreateView
# Create your views here.


class ReviewView(CreateView):  # FormView  #View
    model: Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def form_valid(self, form):  #This is not need as we used the CreatView
    #     form.save()
    #     return super().form_valid(form)

    # class ReviewView(View):
    #     def get(self, request):
    #         form = ReviewForm()

    #         return render(request, "reviews/review.html", {
    #             "form": form
    #         })

    #     def post(self, request):
    #         form = ReviewForm(request.POST)

    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect("/thank-you")

    #         return render(request, "reviews/review.html", {
    #             "form": form
    #         })

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

class ReviewsListView(ListView):  # Listview=To show all list of content
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


# DetailView= To show details of hte content
# class DetailReviewView(TemplateView):
#     template_name = "reviews/detailed_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/detailed_review.html"
