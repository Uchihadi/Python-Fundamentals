#lex_auth_01269437504257228837

def find_average(mark_list):
	total=0
 
	try:
		for i in range(0, len(mark_list)):
			total+=mark_list[i]
		marks_avg=total/len(mark_list)
		return marks_avg

	except NameError:
     	 print("Name error Occured")
       
	# except ValueError:
    #  	 print("Value error Occured")
       
	# except TypeError:
	# 	print ("Type Error Occurred")
     

m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))