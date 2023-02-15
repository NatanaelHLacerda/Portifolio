from django.db import models
from Rotas.mapa import mapa
import json

# Create your models here.


class engine(models.Model):
    mapeamento = mapa
    mapa_serializado = models.TextField

    def set_dicionario(self, mapeamento):
        self.mapa_serializado = json.dumps(mapeamento)

    def get_dicionario(self):
        return json.loads(self.mapa_serializado)