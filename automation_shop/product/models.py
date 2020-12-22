from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categories'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,null=True, blank=True, related_name='products',
                                 on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, db_index=True, default="")
    slug = models.SlugField(max_length=200, db_index=True, default="")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


