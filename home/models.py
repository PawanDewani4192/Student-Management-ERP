from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=13)
    qualification=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    edt=models.DateField(auto_now=False, auto_now_add=False)
    gch= (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
)
    gender=models.CharField(max_length=7,choices=gch)
    bch= (
    ('cs', 'cs'),
    ('it', 'it'),
    ('ec', 'ec'),
    ('mech', 'mech'),
    ('civil', 'civil'),
    ('nonit', 'nonit'),
)
    branch=models.CharField(max_length=7,choices=bch)
    ych= (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('passout','passout')
)
    year=models.CharField(max_length=8,choices=ych)
    sems= (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('passout','passout')
)
    sem=models.CharField(max_length=8,choices=sems)
    college=models.CharField(max_length=30)
    ch= (
    ('enquiry', 'enquiry'),
    ('joined', 'joined'),
    ('complete', 'complete'),
)
    status=models.CharField(max_length=20,choices=ch)
    def __str__(self) -> str:
        return self.name
class Trainer(models.Model):
    tname=models.CharField(max_length=20)
    mobile=models.CharField(max_length=13)
    email=models.CharField(max_length=30)
    qualification=models.CharField(max_length=20)
    subject=models.CharField(max_length=40)
    timings=models.CharField(max_length=120)
    def __str__(self) -> str:
        return self.tname+self.qualification
class Course(models.Model):
    cname=models.CharField(max_length=40)
    duration=models.CharField(max_length=20)
    fees=models.IntegerField()
    details=models.CharField(max_length=250)
    syllebus=models.FileField(upload_to='files/')
    def __str__(self) -> str:
        return self.cname
class Batch(models.Model):
    bname=models.CharField(max_length=30)
    timing=models.CharField(max_length=40)
    startdate=models.DateField(auto_now=False, auto_now_add=False)
    status=models.CharField(max_length=50)
    Trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    Students=models.ManyToManyField(Student)
    def __str__(self) -> str:
        return self.bname
class Accounts(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Student=models.ForeignKey(Student,on_delete=models.CASCADE)
    total_fees=models.IntegerField()
    first_installment=models.IntegerField()
    first_installment_date=models.DateField(auto_now=False, auto_now_add=False)
    second_installment=models.IntegerField()
    second_installment_date=models.DateField(auto_now=False, auto_now_add=False)
    remaining_amount=models.IntegerField()
    def __str__(self) -> str:
        return str(self.remaining_amount)
