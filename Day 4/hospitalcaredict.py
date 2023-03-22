#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    P_count = 0
    O_count = 0
    E_count = 0
     
    for values in patient_medical_speciality_list:
        if (values == 'P'):
            P_count += 1
        elif (values == 'O'):
            O_count += 1
        elif (values == 'E'):
            E_count += 1
    
    if P_count > O_count and P_count > E_count:
        speciality = medical_speciality ["P"] #Calling the value from dictionary use []
    elif O_count > P_count and O_count > E_count:
        speciality = medical_speciality ["O"]
    else:
        speciality = medical_speciality ["E"]
    
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list= [301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality= {"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality= max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)