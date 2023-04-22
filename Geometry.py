shape=int(input(" 1. Circle\n 2. Triangle\n 3. Rectangle\n 4. Square\n 5. sphere\n 6. Cylinder \n 7. Parallelogram\n 8. Cube\n 9. Pentagon\n 10. Cone\n  Choose any shap  "))
if shape==1:
	print("You choose Circle\n 1. Area\n 2. Circumference\n 3. Diameter\n 4. Radius\n Please choose any one formula:")
	formula=int(input("Enter Formula : "))
	if formula==1:
		redius= int(input("enter redius: "))
		print('area of circle is',3.14*redius**2,'cm2')
	elif formula==2:
		redius=int(input("Enter redius : "))
		print("Circumference of circle is",2*3.14*redius, "Cm" )
	elif formula==3:
		redius=int(input("Enter Redius : "))
		print("Diameter of circle is " ,2*redius)
	elif formula==4:
		diameter=int(input("Enter diameter : "))
		print("Redius of circle is", diameter/2,"cm" )
elif shape==2:
	print(" 1. Perimeter\n 2. Semiperimeter\n 3. Height\n 4. prove it is a triangle\n Please choose any one formula : ")
	formula=int(input("Enter Formula : "))
	if formula==1:
		angle1=int(input("Enter angle 1 : "))
		angle2=int(input("Enter angle 2 : "))
		angle3=int(input("Enter angle 3 : "))
		print("perimeter of triangle is",angle1 +angle2+angle3)
	elif formula==2:
		angle1=int(input("enter angle 1 : "))
		angle2=int(input("enter angle 2 : "))
		angle3=int(input("enter angle 3 : "))
		semiperimeter= angle1+angle2+angle3
		print("semiperimeter of triangle is", semiperimeter/2)
	elif formula==3:
		area=int(input("enter area : "))
		base=int(input("enter base : "))
		height = area/base
		print("Height of triangle is " , height*2)
	elif formula==4:
		angle1=int(input("enter angle 1 : "))
		angle2=int(input("enter angle 2 : "))
		angle3=int(input("enter angle 3 : "))
		a=angle1+angle2+angle3
		if a==180 :
			print("This is a triangle")
		else:
			print("This is not a Triangle")
elif shape==3:
	print(" 1. Perimeter\n 2. length\n 3. width\n Please choose any one formula : ")
	formula=int(input("enter fromula : "))
	if formula==1:
		length=int(input("enter lenth : "))
		width=int(input("enter width : "))
		perimeter=length+width
		print("Perimeter of rectangle is ",perimeter*2)
	elif formula==2:
		width=int(input("enter width : "))
		perimeter=int(input("enter perimeter : "))
		print("length of rectangle is",perimeter/2-width)
	elif formula==3:
		perimeter=int(input("enter perimeter : "))
		length=int(input("enter length : "))
		print("width of ractangle is",perimeter/2-length)
elif shape==4:
	print(" 1. area\n 2. perimeter\n Please choose any one formula : ")
	formula=int(input("enter formula : "))
	if formula==1:
		area=int(input("enter area : "))
		print("Area of square is",area**2)
	elif formula==2:
		perimeter=int(input("Enter perimeter : "))
		print("Perimeter of square is",4*perimeter)
elif shape ==5:
	print(" 1. Diameter\n 2. Volume\n 3. Surface area\n Please choose any one formula")
	formula=int(input("Enter formula : "))
	if formula==1:
		radius=int(input("Enter diameter : "))
		print("Diameter of sphere is", 2*radius)
	elif formula==2:
		radius=int(input("Enter redius : "))
		print("Volume of sphare is",(4/3)*3.14*radius**3)
	elif formula==3:
		radius=int(input("Enter surface area : "))
		print("Surface area of sphare is",4*3.14*radius**2)
elif shape ==6:
	print(" 1. Curved Surface Area of Cylinder\n 2. Total Surface Area of Cylinder\n 3. Volume of Cylinder\n Please choose any one formula ")
	formula=int(input("Enter formula : "))
	if formula==1:
		radius=int(input("Enter radius : "))
		height=int(input("Enter Height : "))
		print("Curved Surface Area of Cylinder is",2*3.13*radius*height)
	elif formula==2:
		radius=int(input("Enter radius : "))
		height=int(input("Enter Height : "))
		print("Total Surface Area of Cylinder is",2*3.13*radius*radius+height)
	elif formula==3:
		radius=int(input("Enter radius : "))
		height=int(input("Enter Height : "))
		print("Volume of Cylinder is" ,3.14*radius**2*height)
elif shape==7:
	print(" 1.Area of Parallelogram\n 2.Perimeter of Parallelogram\n Please choose any one")
	formula=int(input("Enter Formula : "))
	if formula==1:
		base=int(input("Enter Base : "))
		height=int(input("Enter Height : "))
		print("Area of Parallelogram is",base*height)
	elif formula==2:
		base=int(input("Enter base : "))
		height=int(input("Enter height : "))
		print("Area of Parallelogram is",2*base+height)
elif shape==8:
		print(" 1. Total surface Area\n 2. Leteral surface Area\n 3. Volume\n Choose any One ")
		formula=int(input("Enter formula : "))
		if formula==1:
			side=int(input("Enter side : "))
			print("Total surface Area is",6*side**2)
		elif formula==2:
			side=int(input("Enter side : "))
			print("Lateral surface Area is",4*side**2)
		elif formula==3:
			side=int(input("Enter side : "))
			print("Volume of cube is",side**3)
elif shape==9:
	print( "What you do want \n 1. Area\n 2. Perimeter\n 3. lenght\n Please Choose any one")
	formula=int(input("Enter Formula : "))
	if formula==1:
		perimeter=int(input("Enter Perimeter : "))
		length=int(input("Enter Length : "))
		print("Area of Pentagon is " ,5/2*perimeter*length)
	elif formula==2:
		area=int(input("Enter area : "))
		print("Perimeter of Pentagon",5*area)
	elif formula==3:
		area=int(input("Enter Area : "))
		perimeter=int(input("Enter Perimeter : "))
		print("Lenth of Pentagon" ,area*2/perimeter*5)
elif shape==10:
	print("What you want\n 1. Area\n 2. Volume\n please Choose any one")
	formula=int(input("Enter Formula : "))
	if formula==1:
		radius=int(input("Enter Radius : "))
		length=int(input("Enter Length : "))
		print("Area of cone is",22/7*radius+length)
	elif formula==2:
		radius=int(input("Enter radius : "))
		height=int(input("Enter Height : "))
		print("Volume of height is ",1/3*22/7*radius*radius*height)
else:
	print("You choose Wrong option\n please choose Right shape")