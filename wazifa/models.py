from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.



JOB_TYPE=(
    ('Full Time','Full time'),
    ('Part Time', 'Part time')

)

# image upload customiztion
def img_upload(instance,filename):
    imgname , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)


class Job(models.Model):
    # الشخص الي ضاف الوظيفة
    owner = models.ForeignKey(User, related_name='job_owner',on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    job_type = models.CharField (max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    # then make this and makemidration
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=img_upload)

    slug = models.SlugField(blank=True, null=True)

# slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)


    def __str__(self):
        return self.title

# make this first and makemidration
class Category(models.Model):
    name  =   models.CharField( max_length=50 )

    def __str__(self):
        return self.name



# apply form model
class Apply(models.Model):
  job = models.ForeignKey(Job, related_name='apply_job' ,on_delete=models.CASCADE)
  name = models.CharField( max_length=50)
  email = models.EmailField(max_length=100)
  website = models.URLField(max_length=200)
  cv = models.FileField(upload_to='apply/', max_length=100)
  cover_letter = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.name
  