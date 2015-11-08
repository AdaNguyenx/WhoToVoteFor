from django import forms

class SomeForm(forms.Form):
	YES = 1
	NO = 0
	CHOICES = ((YES,'yes'), (NO,'no'),)
	answer1 = forms.MultipleChoiceField(choices=CHOICES)
	answer2 = forms.MultipleChoiceField(choices=CHOICES)
	answer3 = forms.MultipleChoiceField(choices=CHOICES)
	answer4 = forms.MultipleChoiceField(choices=CHOICES)
	answer5 = forms.MultipleChoiceField(choices=CHOICES)
	answer6 = forms.MultipleChoiceField(choices=CHOICES)
	answer7 = forms.MultipleChoiceField(choices=CHOICES)
	answer8 = forms.MultipleChoiceField(choices=CHOICES)
	answer9 = forms.MultipleChoiceField(choices=CHOICES)
	answer10 = forms.MultipleChoiceField(choices=CHOICES)
	state = forms.CharField(max_length=2)



