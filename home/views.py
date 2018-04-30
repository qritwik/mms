from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from home.forms import HomeForm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as pt
from django.core.files.storage import FileSystemStorage
#from home.work import marks

def index(request):
	return render(request,'index.html')

# def internal(request):
# 	return render(request,'internal.html')	

def external(request):
	return render(request,'external.html')	

def pass_fail_view(request):
	xlsx = pd.ExcelFile("newmarks.xlsx")
	sheet1 = xlsx.parse(0)
	df = pd.DataFrame(sheet1)
	df.set_index('USN',inplace=True)
	c_total=df.Name.count()
	sub_code = input("Enter subject code : ")
	s1=sub_code.upper()

	df1=df[df[s1]<12]
	print (df1.Name)
	return render(request,'pass_fail.html')

def range_marks_view(request):
	xlsx = pd.ExcelFile("newmarks.xlsx")
	sheet1 = xlsx.parse(0)
	df = pd.DataFrame(sheet1)
	df.set_index('USN',inplace=True)
	c_total=df.Name.count()
	sub_code = input("Enter subject code : ")
	s1=sub_code.upper()

	df1=df[df[s1]<12]
	c_fail=df1.Name.count()
	c_pass = c_total-c_fail
	sizes=[c_fail,c_pass]
	label=['Fail','Pass']
	color=['red','skyblue']
	plt.pie(sizes,labels=label,colors=color,autopct='%.1f%%')
	plt.axis('equal')
	plt.show()

	return render(request,'range_marks.html')

def list_view(request):
	xlsx = pd.ExcelFile("newmarks.xlsx")
	sheet1 = xlsx.parse(0)
	df = pd.DataFrame(sheet1)
	df.set_index('USN',inplace=True)
	c_total=df.Name.count()
	sub_code = input("Enter subject code : ")
	s1=sub_code.upper()

	df2=df[df[s1]<=5]
	ls_5=df2.Name.count()

	df3=df[(df[s1]>5)&(df[s1]<=10)]
	bt_5_10=df3.Name.count()

	df4=df[(df[s1]>10)&(df[s1]<=15)]
	bt_10_15=df4.Name.count()

	df5=df[df[s1]>15]
	gt_15=df5.Name.count()

	x= ['Less than 5','Btw 5 and 10','Btw 10 and 15','More than 15']
	y= [ls_5,bt_5_10,bt_10_15,gt_15]
	x_pos=[i for i, _ in enumerate(x)]

	pt.bar(x_pos,y,align='center')
	pt.xticks(x_pos,x)
	pt.xlabel('Range')
	pt.ylabel('Count of students')
	pt.title('Range wise marks')
	pt.show()
	return render(request,'list.html')

def individual(request):
	return render(request,'individual.html')

def upload_file(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		print(filename)
		uploaded_file_url = fs.url(filename)
		print(uploaded_file_url)
		return render(request, 'internal.html',)
	return render(request, 'internal.html')	

	

