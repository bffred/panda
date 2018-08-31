from django.db import models

# Create your models here.


class Panda_Geant(models.Model):
    surnom = models.CharField(max_length =50, verbose_name= 'Surnom')
    ordre = models.CharField(max_length =50)
    famille = models.CharField(max_length =50)
    classe = models.CharField(max_length =50)


    def __str__(self):
        return self.surnom

    class Meta:
        verbose_name = "Panda_Géant"


# Surnom
# Ordre : Carnivora
# Famille : Ursidae
# Classe : Mammalia
# Poids : Femelle: 70 – 100 kg (Adulte)
# Espérance de vie : 20 ans (À l'état sauvage)
# Période de gestation : 95 – 160 jours