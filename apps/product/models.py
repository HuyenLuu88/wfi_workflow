from django.db import models
from apps.portfolio.models import Identifier

# Create your models here.





class Wca(models.Model):
    secid = models.IntegerField(blank=False, null=False)
    isin = models.CharField(max_length=12, null=True)
    #isin = models.ForeignKey(Identifier, on_delete=models.DO_NOTHING, null=True)
    uscode = models.CharField(max_length=9)
    #uscode = models.ForeignKey(Identifier, on_delete=models.DO_NOTHING, null=True)
    sedol = models.CharField(max_length=7)
    #sedol = models.ForeignKey(Identifier, on_delete=models.DO_NOTHING, null=True)
    issuername = models.CharField(max_length=70)
    sectycd = models.CharField(max_length=3)
    bondtype = models.CharField(max_length=10)
    securitydesc = models.CharField(max_length=70)
    statusflag = models.CharField(max_length=1)


    def __str__(self):
        return self.secid

    class Meta:
        verbose_name_plural = "WCA"