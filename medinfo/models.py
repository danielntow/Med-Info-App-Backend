from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields you may need for the drug


class Dosage(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    description = models.TextField()


class AdverseEffect(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    description = models.TextField()


class Indication(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    description = models.TextField()


class Warning(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    description = models.TextField()


class Administration(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    description = models.TextField()


class PregnancyLactation(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    description = models.TextField()


class Contraindication(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    description = models.TextField()
