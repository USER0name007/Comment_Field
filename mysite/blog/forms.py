from django import forms


class CommentForm(forms.Form):
	name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"type":"text", "name":"fname","placeholder":"Name"}))
	comment = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "name":"comment","class":"commm", "placeholder": "comment"}))
	