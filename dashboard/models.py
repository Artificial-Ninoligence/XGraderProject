from django.db import models

# Create your models here.
class Schedule(models.Model):
    """ Schedule is the main entry point to all other data in the data base """

    title           = models.CharField(max_length=250)
    semester        = models.CharField(max_length=250)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    """ Each module has its own grade for the user """

    title           = models.CharField(max_length=250)
    grade           = models.IntegerField(blank=True)
    attempt         = models.IntegerField(blank=True)
    is_registered   = models.BooleanField(default=False)

    #* OneToMany Relationship: One schedule for a specific semester can have many modules
    schedule        = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Assessment(models.Model):
    """ How a module will be assessed and one module will have many assessments """

    ORAL_ASSESSMENT = "OA"
    WRITTEN_ASSESSMENT = "WA"
    EARLY_ASSESSMENT = "EA"
    ALTERNATIVE_ASSESSMENT = "AA"
    STANDARD_ASSESSMENT = "SA"

    ASSESSMENT_CHOICES = [
       (ORAL_ASSESSMENT, ('Oral Assessment')),
       (WRITTEN_ASSESSMENT, ('Written Assessment')),
       (EARLY_ASSESSMENT, ('Early Assessment')),
       (ALTERNATIVE_ASSESSMENT, ('Alternative Assessment')),
       (STANDARD_ASSESSMENT, ('Standard Assessment'))
    ]

    assessment_type = models.CharField(max_length=32, choices=ASSESSMENT_CHOICES, default=STANDARD_ASSESSMENT)
    assessment_date = models.DateTimeField(auto_now_add=False)
    target_grade    = models.IntegerField(blank=True)
    requirements    = models.CharField(max_length=500)
    created_at      = models.DateTimeField(auto_now_add=True)

    #* OneToMany Relationship: One module might have more than one assessment
    module          = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.assessment_type
