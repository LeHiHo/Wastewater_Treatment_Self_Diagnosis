from django.db import models

class Wastedata(models.Model):
    name = models.CharField(max_length=20)

    targetBOD = models.DecimalField(max_digits=3, decimal_places=1)
    targetTSS = models.DecimalField(max_digits=3, decimal_places=1)
    targetTN = models.DecimalField(max_digits=3, decimal_places=1)
    targetTP = models.DecimalField(max_digits=3, decimal_places=1)

    wasteInflow = models.DecimalField(max_digits=9, decimal_places=2)
    wasteInputBOD = models.DecimalField(max_digits=7, decimal_places=3)
    wasteInputTSS = models.DecimalField(max_digits=7, decimal_places=3)
    wasteInputTN = models.DecimalField(max_digits=7, decimal_places=3)
    wasteInputTP = models.DecimalField(max_digits=7, decimal_places=3)

    wasteOutflow = models.DecimalField(max_digits=9, decimal_places=2)
    wasteOutputBOD = models.DecimalField(max_digits=7, decimal_places=3)
    wasteOutputTSS = models.DecimalField(max_digits=7, decimal_places=3)
    wasteOutputTN = models.DecimalField(max_digits=7, decimal_places=3)
    wasteOutputTP = models.DecimalField(max_digits=7, decimal_places=3)

    RemoveBOD = models.DecimalField(max_digits=3, decimal_places=1)
    RemoveTSS = models.DecimalField(max_digits=3, decimal_places=1)
    RemoveTN = models.DecimalField(max_digits=3, decimal_places=1)
    RemoveTP = models.DecimalField(max_digits=3, decimal_places=1)
    
    BODdecision = models.BooleanField()
    TSSdecision = models.BooleanField()
    TNdecision = models.BooleanField()
    TPdecision = models.BooleanField()


    def __str__(self):
        return self.name
