from django.db import models

# Create your models here.



JOB_TYPE=(
    ('Full Time','Full time'),
    ('Part Time', 'Part time')

)



class Job(models.Model):
    title = models.CharField(max_length=150)
    job_type = models.CharField (max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)














    def __str__(self):
        return self.title
    