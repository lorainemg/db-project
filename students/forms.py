from django import forms 
from students.models import Student

class name(forms.Form): 
    q = forms.DecimalField() 

    # def clean_q(self):
    # 	q = self.cleaned_data['q']
    # 	if not q[0].isupper():
    # 		raise forms.ValidationError("¡criterio de busqueda muy pequeno!") 
    # 	return q

class Form(forms.Form): 
    ci = forms.DecimalField()
    tel = forms.DecimalField(required=False)
    nombre = forms.CharField()
    pApellido = forms.CharField()
    sApellido = forms.CharField()
    email = forms.EmailField(required=False)
    calle = forms.CharField()
    num = forms.DecimalField()
    apto = forms.CharField()
    esc = forms.CharField()
    entre = forms.CharField()
    y = forms.CharField()
    repa = forms.CharField()
    poblado = forms.CharField()
    mun = forms.CharField()
    cod0 = forms.CharField()
    prov = forms.CharField()
    cod = forms.CharField()
    color = (
    ('1', 'Negro'),
    ('2', 'Blanco'),
    ('3', 'Mestizo'),
    )
    colorRadio = forms.ChoiceField(widget=forms.RadioSelect, choices=color)
    sex = (
    ('1', 'Femenino'),
    ('2', 'Masculino'),
    )
    colorSexo = forms.ChoiceField(widget=forms.RadioSelect, choices=sex)
    places = (
    ('1', 'IPU'),
    ('2', 'Politecnico'),
    ('3', 'FOC'),
    ('4', 'Otro'),
    )
    procedencia = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=places)
    ocupation = (
    ('1', 'Dirigente'),
    ('2', 'Profesional'),
    ('3', 'Tecnico'),
    ('4', 'Administrativo'),
    ('5', 'Trabajador de los servicios'),
    ('6', 'Obrero'),
    ('7', 'Campesino'),
    ('8', 'Ama de casa'),
    ('9', 'Otra situación'),
    )
    ocupacionRadio = forms.ChoiceField(widget=forms.RadioSelect, choices=ocupation)
    OtroV = forms.CharField(required=False)
    vinculo = (
    ('1', 'Sí'),
    ('2', 'No'),
    )
    vinculaRadio = forms.ChoiceField(widget=forms.RadioSelect, choices=vinculo)
    sector = (
    ('1', 'Estatal'),
    ('2', 'Privado'),
    ('3', 'Cooperativo'),
    ('4', 'Mixto o Extranjero'),
    )
    sectorRadio = forms.ChoiceField(widget=forms.RadioSelect, choices=sector)

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            return email
        return email.lower()
    

    def clean_ci(self):
        ci = self.cleaned_data['ci']
        if ci < 10**10 or ci >= 10**11:
            raise forms.ValidationError("¡carnet de id muy corto!") 
        search = Student.objects.filter(CI__icontains = ci)
        if len(search) > 0:
            raise forms.ValidationError("ya se encuentra el id en la base de datos!") 
        return ci
    # def clean_q(self):
    # 	q = self.cleaned_data['q']
    # 	if not q[0].isupper():
    # 		raise forms.ValidationError("¡criterio de busqueda muy pequeno!") 
    # 	return q
    