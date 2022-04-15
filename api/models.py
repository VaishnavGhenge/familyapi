from django.db import models

class Child(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    family = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name + ' ' + str(self.family)

class Family(models.Model):
    _id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=200)
    parent1 = models.CharField(max_length=200)
    parent2 = models.CharField(max_length=200)

    def __str__(self):
        return self.surname