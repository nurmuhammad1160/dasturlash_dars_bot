from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    email = models.CharField(verbose_name='Email', max_length=50, null=True)


    class Meta:
        db_table = 'all_users'

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        db_table = 'category'
    

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"name: {self.name} category: {self.category}"
    
    class Meta:
        db_table = 'subcategory'

         

class Lesson(models.Model):
    dars_soni = models.IntegerField()
    video_id = models.CharField(max_length=255)
    info = models.TextField()
    youtube = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.category}--{self.subcategory}--{self.dars_soni}-dars"
    
    class Meta:
        db_table = 'lesson'
    



