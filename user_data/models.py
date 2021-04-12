from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=40)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.rua) + '  ' + str(self.bairro) + ' ' + str(self.cidade)
    
class UserData(models.Model):
    nome_completo = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    profile_photo = models.FileField(upload_to='profile/',blank=True, null=True)
    

