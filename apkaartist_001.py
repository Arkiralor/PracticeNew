from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    name = models.CharField(max_length = 32, null=False, blank=False, default='', verbose_name='full_name')
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='joined', null=False)

resp = User.objects.filter(
        (
            models.Q(name_icontains = "Akash") 
            | models.Q(name_icontains = "Prithoo" ) 
        )
        & models.Q(email__startswith = "a")
    )

resp = User.objects.get(pk=1) #= QuerySet
resp = User.objects.filter(id=1) #= List[Queryset]