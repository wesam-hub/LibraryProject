from django import forms
from .models import Book , Category

class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-primary'
            visible.field.widget.attrs['placeholder'] = 'Write category here'

    class Meta:
        model = Category
        fields = ['name']


        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control text'})

        # }


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-primary'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            self.fields['rental_price_day'].widget = forms.TextInput(attrs={'id': 'rentalprice','class':'form-control text-primary','placeholder':'rental price'})
            self.fields['rental_period'].widget = forms.TextInput(attrs={'id': 'rentalperiod','class':'form-control text-primary','placeholder':'rental period'})
            self.fields['total_rental'].widget = forms.TextInput(attrs={'id': 'totalrental','class':'form-control text-primary','placeholder':'total rental'})
            
            self.fields['title'].widget.attrs['placeholder'] = 'Write title here'

    class Meta:
        model = Book
        #fields = '__all__' # لو عايزة كل الحقول 
        fields = [
            'title',
            'author',
            'photo_book',
            'phot_author',
            'pages',
            'price',
            'rental_price_day',
            'rental_period',
            'total_rental',
            'status',
            'category',
            
        ]  # لو عايزة حقول معينة
        
        # widgets = {
        #     'title':forms.TextInput(attrs={'class':'form-control'}),
        #     'author':forms.TextInput(attrs={'class':'form-control'}),
        #     'photo_book':forms.FileInput(attrs={'class':'form-control'}),
        #     'phot_author':forms.FileInput(attrs={'class':'form-control'}),
        #     'pages':forms.NumberInput(attrs={'class':'form-control'}),
        #     'price':forms.NumberInput(attrs={'class':'form-control'}),
        #     'rental_price_day':forms.NumberInput(attrs={'class':'form-control'}),
        #     'rental_period':forms.NumberInput(attrs={'class':'form-control'}),
        #     'status':forms.Select(attrs={'class':'form-control'}),
        #     'category':forms.Select(attrs={'class':'form-control'})
        # }
