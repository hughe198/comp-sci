from django.views.generic import ListView
from django.shortcuts import render
from content.models import HomePageTopPost, GalleryImage, Topic

from django.contrib.auth.decorators import login_required

from content.models import QuestionSet


class HomePage(ListView):
    template_name = "index.html"
    model = HomePageTopPost

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context['galleryimages_list'] = GalleryImage.objects.all()
        return context


@login_required(login_url="/login/")
def student_login(request):
    topic = Topic.objects.all()
    units = topic.order_by().values_list('unit_name',
                                         flat=True).distinct()
    # find distinct() topic units to catorgise student_home page topics.
    context = {'topic': topic, 'units': units}
    return render(request, 'student_home.html', context)


@login_required(login_url="/login/")
def topicdetailview(request, pk):
    topic = Topic.objects.get(id=pk)
    list_quizes = topic.questionset_set.all()
    context = {'list_quizes': list_quizes, 'topic': topic}
    return render(request, 'topic_detail.html', context)


@login_required(login_url="/login/")
def quiz(request, pk):
    quiz_element = QuestionSet.objects.get(id=pk)
    questions = []
    for q in quiz_element.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a)
        questions.append({q: answers})
    context = {'questions': questions}
    print(context)
    type(context )
    return render(request, 'quiz.html', context)
