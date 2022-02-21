from django.shortcuts import render
from .models import Accounts,Course,Student,Trainer,Batch
from django.core import serializers
import datetime
def home(request):
    return render(request,"home.html")
                            #studentcrud
def addstudent(request):
    if request.method=='POST':
        s=Student()
        s.name=request.POST['name']
        s.email =request.POST['email']
        s.mobile =request.POST['mobile']
        s.address =request.POST['address']
        s.qualification=request.POST['qualification']
        s.branch=request.POST['bch']
        s.gender=request.POST['gch']
        s.year=request.POST['ych']
        s.sem=request.POST['sch']
        s.status=request.POST['ch']
        s.college=request.POST['college']
        s.edt=datetime.datetime.now().date()
        s.save()
        st=Student.objects.all()
        return render(request,'addstudent.html',{'st':st})
    else:
       st=Student.objects.all()
       return render(request,'addstudent.html',{'st':st})
def showstudent(request):
    S=Student.objects.all()
    return render(request,'showStudent.html',{'S':S})
def studentdelete(request):
    id=request.GET['id']
    Student.objects.filter(id=id).delete()
    S=Student.objects.all()
    return render(request,'showStudent.html',{'S':S})
def studentupdate(request):
    id=request.POST['id']
    S=Student.objects.filter(id=id).get()
    S.name=request.POST['name']
    S.email=request.POST['email']
    f=request.POST['mobile']
    S.mobile=int(f)
    S.qualification=request.POST['qualification']
    S.address=request.POST['address']
    S.gender=request.POST['gender']
    S.branch=request.POST['branch']
    S.year=request.POST['year']
    S.sem=request.POST['sem']
    S.status=request.POST['status']
    S.save()
    S=Student.objects.all()
    return render(request,'showStudent.html',{'S':S})
                                        #trainercrud
def addtrainer(request):
    if request.method=='POST':
        a=Trainer()
        a.tname=request.POST['tname']
        a.mobile =request.POST['mobile']
        a.email =request.POST['email']
        a.qualification =request.POST['qualification']
        a.subject =request.POST['subject']
        a.timings=request.POST['timings']
        a.save()
        tr=Trainer.objects.all()
        return render(request,'addtrainer.html',{'tr':tr})
    else:
        tr=Trainer.objects.all()
        return render(request,'addtrainer.html',{'tr':tr})
def showtrainer(request):
    data=Trainer.objects.all()
    return render(request,'showtrainer.html',{'data':data})
def updatetrainer(request):
    id=request.POST['id']
    t=Trainer.objects.filter(id=id).get()
    t.tname=request.POST['tname']
    t.mobile =request.POST['mobile']
    t.email =request.POST['email']
    t.qualification =request.POST['qualification']
    t.subject =request.POST['subject']
    t.timings=request.POST['timings']
    t.save()
    data=Trainer.objects.all()
    return render(request,'showtrainer.html',{'data':data})
def deletetrainer(request):
    id=request.GET['id']
    Trainer.objects.filter(id=id).delete()
    data=Trainer.objects.all()
    return render(request,'showtrainer.html',{'data':data})
                                #coursecrud
def addcourse(request):
    if request.method=='POST':
        c=Course()
        c.cname=request.POST['cname']
        c.duration =request.POST['duration']
        c.fees=request.POST['fees']
        c.details=request.POST['details']
        c.syllebus=request.POST['syllebus']
        c.save()
        cr=Course.objects.all()
        return render(request,'addcourse.html',{'cr':cr})
    else:
       cr=Course.objects.all()
       return render(request,'addcourse.html',{'cr':cr})
def showcourse(request):
    cr=Course.objects.all()
    return render(request,'showcourse.html',{'cr':cr})
def deletecourse(request):
    id=request.GET['id']
    Course.objects.filter(id=id).delete()
    cr=Course.objects.all()
    return render(request,'showcourse.html',{'cr':cr})
def updatecourse(request):
    id=request.POST['id']
    c=Course.objects.filter(id=id).get()
    c.cname=request.POST['cname']
    c.duration =request.POST['duration']
    c.fees=request.POST['fees']
    c.details=request.POST['details']
    c.save()
    cr=Course.objects.all()
    return render(request,'showcourse.html',{'cr':cr})
                                    #accountcrud
def addaccount(request):
    if request.method=='POST':
        a=Accounts()
        a.total_fees=request.POST['tfees']
        a.first_installment =request.POST['finst']
        a.first_installment_date =request.POST['finst_date']
        second = request.POST['sinst']
        
        if(second == ''):
            second = 0
            a.second_installment = second
        else:
            a.second_installment = second
            
        a.second_installment_date =request.POST['sinst_date']
        a.remaining_amount=request.POST['remainfee']
        cid=request.POST['course']
        a.course=Course.objects.filter(id=cid).get()
        id=request.POST['student']
        a.Student=Student.objects.filter(id=id).get()
        a.save()
        cour=Course.objects.all()
        stu=Student.objects.all()
        return render(request,'addaccount.html',{'cour':cour,'stu':stu})
    else:
        cour=Course.objects.all()
        stu=Student.objects.all()
        cr = Course.objects.all()
        qs_json=serializers.serialize('json', cr)
        return render(request,'addaccount.html',{'cour':cour,'stu':stu,'jsondata':qs_json})
    
def showaccount(request):
    Ac=Accounts.objects.all()
    return render(request,'showaccount.html',{'Ac':Ac})

def updateaccount(request):
    id=request.POST['id']
    a=Accounts.objects.filter(id=id).get()
    a.total_fees=request.POST['tfees']
    a.first_installment=request.POST['finst']
    a.first_installment_date=request.POST['finst_date']
    a.second_installment=request.POST['sinst']
    a.second_installment_date=request.POST['sinst_date']
    a.remaining_fees=request.POST['remainfee']
    cid=request.POST['courses']
    c=Course.objects.filter(id=cid).get()
    a.course=c
    sid=request.POST['students']
    s=Student.objects.filter(id=sid).get()
    a.student=s
    s.save()
    Ac=Accounts.objects.all()
    cour=Course.objects.all()
    stu=Student.objects.all()
    return render(request,'showaccount.html',{'Ac':Ac,'cour':cour,'stu':stu})

def deleteaccount(request):
    id=request.GET['id']
    Accounts.objects.filter(id=id).delete()
    Ac=Accounts.objects.all()
    cour=Course.objects.all()
    stu=Student.objects.all()
    return render(request,'showaccount.html',{'Ac':Ac,'cour':cour,'stu':stu})

                            #crudbatch
def addbatch(request):
    if request.method=='POST':
        b=Batch()
        print(request.POST)
        b.bname=request.POST['bname']
        b.timing =request.POST['timing']
        b.startdate =request.POST['startdate']
        b.status =request.POST['status']
        tid=request.POST['Trainer']
        b.Trainer=Trainer.objects.filter(id=tid).get()
        b.save()
        s=request.POST.getlist('Student')
        for id in s:
            s1=Student.objects.filter(id=id).get()
            b.Students.add(s1)
        st=Student.objects.all()
        tr=Trainer.objects.all()
        return render(request,'addbatch.html',{'st':st,'tr':tr})
    else:
        st=Student.objects.all()
        tr=Trainer.objects.all()
        return render(request,'addbatch.html',{'st':st,'tr':tr})
    
def showbatch(request):
    bt=Batch.objects.all()
    st=Student.objects.all()
    tr=Trainer.objects.all()
    return render(request,'showbatch.html',{'bt':bt,'st':st,'tr':tr})

def deletebatch(request):
    id=request.GET['id']
    Batch.objects.filter(id=id).delete()
    bt=Batch.objects.all()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'showbatch.html',{'bt':bt,'tr':tr,'st':st})
def updatebatch(request):
    id=request.POST['id']
    b=Batch.objects.filter(id=id).get()
    b.bname=request.POST['bname']
    b.timing =request.POST['timing']
    b.startdate =request.POST['startdate']
    b.status =request.POST['status']
    tid=request.POST['Trainer']
    t=Trainer.objects.filter(id=tid).get()
    b.course=t
    b.save()
    bt=Batch.objects.all()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'showbatch.html',{'bt':bt,'tr':tr,'st':st})
def serachenquiry(request):
    if request.method=='POST':
        fdate=request.POST['fdate']
        tdate=request.POST['tdate']
        S=Student.objects.filter(edt__range=(fdate, tdate)).all()
        return render(request,'showStudent.html',{'S':S})
    else:
        return render(request,'serachenquiry.html')
def searchaccount(request):
    if request.method=='POST':
        fdate=request.POST['fdate']
        tdate=request.POST['tdate']
        ch=request.POST['ch']
        Ac=None
        if ch=='paid_first':
            Ac=Accounts.objects.filter(first_installment_date__range=(fdate, tdate)).all()
        elif ch=='paid_second':
            Ac=Accounts.objects.filter(second_installment_date__range=(fdate, tdate)).all()
        else:
            Ac=Accounts.objects.filter(second_installment_date__range=(fdate, tdate)).all()
        return render(request,'showaccount.html',{'Ac':Ac})
    else:
        return render(request,'searchaccount.html')