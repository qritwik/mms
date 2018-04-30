# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.pyplot as pt

# class marks():
# 	xlsx = pd.ExcelFile("newmarks.xlsx")
# 	sheet1 = xlsx.parse(0)
# 	df = pd.DataFrame(sheet1)
# 	df.set_index('USN',inplace=True)
# 	c_total=df.Name.count()
# 	sub_code = input("Enter subject code : ")
# 	s1=sub_code.upper()

# 	def pass_fail(s1):
# 		df1=df[df[s1]<12]
# 		print (df1.Name)

# 	def display_piechart(s1,c_total):
# 		df1=df[df[s1]<12]
# 		c_fail=df1.Name.count()
# 		c_pass = c_total-c_fail
# 		sizes=[c_fail,c_pass]
# 		label=['Fail','Pass']
# 		color=['red','skyblue']
# 		plt.pie(sizes,labels=label,colors=color,autopct='%.1f%%')
# 		plt.axis('equal')
# 		plt.show()

# 	def display_bar(s1):
# 		df2=df[df[s1]<=5]
# 		ls_5=df2.Name.count()

# 		df3=df[(df[s1]>5)&(df[s1]<=10)]
# 		bt_5_10=df3.Name.count()

# 		df4=df[(df[s1]>10)&(df[s1]<=15)]
# 		bt_10_15=df4.Name.count()

# 		df5=df[df[s1]>15]
# 		gt_15=df5.Name.count()

# 		x= ['Less than 5','Btw 5 and 10','Btw 10 and 15','More than 15']
# 		y= [ls_5,bt_5_10,bt_10_15,gt_15]
# 		x_pos=[i for i, _ in enumerate(x)]

# 		pt.bar(x_pos,y,align='center')
# 		pt.xticks(x_pos,x)
# 		pt.xlabel('Range')
# 		pt.ylabel('Count of students')
# 		pt.title('Range wise marks')
# 		pt.show()