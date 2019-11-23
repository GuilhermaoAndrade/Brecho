from django import forms
from website.models import Pedido

class PedidoForm(forms.ModelForm):
    #define as caracteristicas doas atributos abaixo
    class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'cartao',
            'pagamento',
        
        ]