#from PIL import Image
#from django import forms
from django.core.files import File
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class VideoForm(forms.ModelForm):
	class Meta:
		model= VideoLibrary
		fields = ['title', 'description', 'image_poster','genre','image_poster', 'files', 'age_restriction', 'year_of_release' ]
