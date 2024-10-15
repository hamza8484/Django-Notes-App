
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    PrdName = models.CharField(max_length=100 ,verbose_name=_("Product Name:"))
    PrdCategory = models.ForeignKey('Category' , on_delete=models.CASCADE , blank=True,null=True ,verbose_name=_("Category:"))
    PRDBrand = models.ForeignKey('settings.Brand',  on_delete=models.CASCADE , blank=True,null=True ,verbose_name=_("Brand:"))
    PrdDesc = models.TextField( verbose_name=_("Description:"))
    PrdImage = models.ImageField(upload_to='product/' , verbose_name=_("Image:") , blank=True,null=True)  
    PrdPrice = models.DecimalField(max_digits=5 , decimal_places=2 ,verbose_name=_("Price:"))
    PrdDiscountPrice = models.DecimalField(max_digits=5 , decimal_places=2 ,verbose_name=_("Discount Price:"))
    PrdCost = models.DecimalField(max_digits=5 , decimal_places=2  ,verbose_name=_("Cost Price:"))
    PrdCreate = models.DateTimeField(verbose_name=_("Created At:"))


    PrdSlug = models.SlugField(blank=True,null=True ,verbose_name=_("Product Url:"))
    PrdIsNew = models.BooleanField(default=True ,verbose_name=_("New Product:"))
    PrdBestseller = models.BooleanField(default=False ,verbose_name=_("Best Seller:"))



    def save(self ,*args , **kwargs ):
        if not self.PrdSlug :
            self.PrdSlug = slugify(self.PrdName)
        super(Product , self).save( *args , **kwargs  )

    class Meta:
        verbose_name = _("Product")   
        verbose_name_plural =_("Products") 
    
    def get_absolute_url(self):
        return reverse('products:product_detail' , kwargs={'slug':self.PrdSlug})

    def __str__(self):
        return self.PrdName
    





class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product:"))
    PRDIImage = models.ImageField(upload_to='product/' , verbose_name=_("Image:"))   

    def __str__(self):
        return str(self.PRDIProduct)
    


class Category(models.Model):
    CATName = models.CharField(max_length=50 , verbose_name=_("Name:"))
    CATParent = models.ForeignKey('self' , limit_choices_to= { 'CATParent__isnull' : True}, verbose_name=_("Main Category:") , on_delete=models.CASCADE , blank=True,null=True)
    CATDesc = models.TextField(verbose_name=_("Description:"))
    CATImg = models.ImageField(upload_to='Category/' , verbose_name=_("Image:") )


    class Meta:
        verbose_name = _("Category")   
        verbose_name_plural =_("Categories") 

    def __str__(self):
        return str(self.CATName)
    

class Product_Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='main_Product' , verbose_name=_("Product:"))
    PALNAlternatives = models.ManyToManyField(Product , related_name='alternative_product' , verbose_name=_("Alternative:"))

    class Meta:
        verbose_name = _("Product Alternative")   
        verbose_name_plural =_("Product Alternatives") 
    
    def __str__(self):
        return str(self.PALNProduct)
    

class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='mainAccessory_Product' , verbose_name=_("Product:") )
    PACCAlternatives = models.ManyToManyField(Product , related_name='accessories_product' , verbose_name=_("Accessories:"))

    class Meta:
       verbose_name = _("Product Accessory")   
       verbose_name_plural =_("Product Accessories") 
    
    def __str__(self):
       return str(self.PACCProduct)

