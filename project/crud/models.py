from django.db import models

class Item(models.Model):

    Name=models.CharField(max_length=300,null=False)

    description=models.TextField(null=True)

    date=models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        
        return self.Name
    
