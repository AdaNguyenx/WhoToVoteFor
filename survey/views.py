
from django.shortcuts import render
from .forms import SomeForm
from django.http import HttpResponseRedirect
from .models import SurveyResponse
from .backend import findLegislators1, findLegislators2

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def marijuana(request):
	return render(request, "marijuana.html", {})

def refugees(request):
	return render(request, "refugees.html", {})

def abortions(request):
	return render(request, "abortions.html", {})

def dealthpenalty(request):
	return render(request, "dealthpenalty.html", {})

def healthcare(request):
	return render(request, "healthcare.html", {})

def globalwarming(request):
	return render(request, "globalwarming.html", {})

def minimumwage(request):
	return render(request, "minimumwage.html", {})

def gunsrights(request):
	return render(request, "gunsrights.html", {})

def education(request):
	return render(request, "education.html", {})

def veterans(request):
	return render(request, "veterans.html", {})

def results1(request):
	state1 = SurveyResponse.objects.all()
	for object in state1:
		userstate1 = object.answer
	legislators1 = findLegislators1(userstate1)
	return render(request, "results1.html", {'legislators1':legislators1})

def results2(request):
	state2 = SurveyResponse.objects.all()
	for object in state2:
		userstate2 = object.answer
	legislators2 = findLegislators2(userstate2)
	return render(request, "results2.html", {'legislators2':legislators2})

def some_view(request):
	someresponse = []
	if request.method == 'POST':

		form = SomeForm(request.POST)
		if form.is_valid():
			answer1 = form.cleaned_data['answer1']
			answer2 = form.cleaned_data['answer2']
			answer3 = form.cleaned_data['answer3']
			answer4 = form.cleaned_data['answer4']
			answer5 = form.cleaned_data['answer5']
			answer6 = form.cleaned_data['answer6']
			answer7 = form.cleaned_data['answer7']
			answer8 = form.cleaned_data['answer8']
			answer9 = form.cleaned_data['answer9']
			answer10 = form.cleaned_data['answer10']
			state = form.cleaned_data['state']
			
			surveyState = SurveyResponse.objects.create(answer = state)
			
			someresponse.append(int(answer1[0]))
			someresponse.append(int(answer2[0]))
			someresponse.append(int(answer3[0]))
			someresponse.append(int(answer4[0]))
			someresponse.append(int(answer5[0]))
			someresponse.append(int(answer6[0]))
			someresponse.append(int(answer7[0]))
			someresponse.append(int(answer8[0]))
			someresponse.append(int(answer9[0]))
			someresponse.append(int(answer10[0]))
			

			responsenumber = sum(someresponse)

			# different legislators for different responsenumber
			# democratic
			if (responsenumber > 6):
				return HttpResponseRedirect('/results1/')
			else: #republican
				return HttpResponseRedirect('/results2/')

	else:
		form = SomeForm

	return render(request,'some_template.html', {'form':form})
