from django.contrib import admin
from .models import Usuario, Imovel, Contrato, Pagamento

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Imovel)
admin.site.register(Contrato)
admin.site.register(Pagamento)