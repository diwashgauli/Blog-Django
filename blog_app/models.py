from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=256)
    content= models.TextField()
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    

#published_at data chaina => null cha 
#published_at data cha => null chaina 


## 1- 1 Relationship 
# 1 user can have only 1 profile =>1
# 1 profile is associated to only 1 user => 1
# OneToOneField()=> Any models

## 1- M Relationship 
# 1 user can add M post => M
# 1 post is associated to only 1 users => 1
# In Django use ForeignKey()=> user in many side models

## M - M Relationship
# 1 student can learn from M teachers => M
# 1 teacher can teach M students => M
# ManyToManyField()=> Any place 


