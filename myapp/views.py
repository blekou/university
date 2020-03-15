from django.shortcuts import render


# Create your views here.
def index(request):

    datas = {

    }
    return render(request, "pages/index.html", datas)

def contact(request):

    datas = {

    }
    return render(request, "pages/contact.html", datas)


def blog(request):

    datas = {

    }
    return render(request, "pages/blog.html", datas)

def courses(request):

    datas = {

    }
    return render(request, "pages/Courses.html", datas)

def single(request):

    datas = {

    }
    return render(request, "pages/single-blog.html", datas)

def elements(request):

    datas = {

    }
    return render(request, "pages/elements.html", datas)

def event(request):

    datas = {

    }
    return render(request, "pages/Event.html", datas)


def details(request):

    datas = {

    }
    return render(request, "pages/event_details.html", datas)

def admissions(request):

    datas = {

    }
    return render(request, "pages/Admissions.html", datas)
