from django import forms
from .model import MapImage

class UploadForm(forms.ModelForm):
	class Meta:
		model=MapImage
		field=('image','name')