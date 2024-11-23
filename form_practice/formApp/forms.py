from django import forms 


class Froms(forms.Form):
    name = forms.CharField(max_length=50, initial='Your name')
    comment = forms.CharField(widget=(forms.Textarea(attrs={'rows':3})), initial='About the form')
    email = forms.EmailField(initial='Your email')
    date = forms.DateField(widget=(forms.NumberInput(attrs={'type': 'date'})))
    age = forms.IntegerField(initial='Enter your date')
    
    FAVORITE_GAME_CHOICES = [ 
        ('gta v','GTA V') , 
        ('metro exodus','Metro Exodus'), 
        ('the wolf among us', 'The Wolf Among Us')
        ]
    Favourite_Game = forms.ChoiceField(choices=FAVORITE_GAME_CHOICES)

    FAVORITE_MOBILE_GAMES = [ 
        ('wrestling revulation 3d','Wrestling Revulation 3D') , 
        ('wwe mayhem','WWE Mayhem'), 
        ('samurai II: vengeance', 'Samurai II: Vengeance')
        ]

    Mobile_Game = forms.MultipleChoiceField(choices=FAVORITE_MOBILE_GAMES)

    FAVORITE_GAME_GENRES = [ 
        ('base game','BASE GAME') , 
        ('rpg','RPG'), 
        ('action', 'ACTION')
        ]
    Favourite_Game_Genre = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_GAME_GENRES)

    HOBBIES = [
        ('swimming', 'Swimming'),
        ('running', 'Running'),
        ('reading books', 'Reading Books')
    ]

    Hobby = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=HOBBIES, required=False)

    agree = forms.BooleanField()