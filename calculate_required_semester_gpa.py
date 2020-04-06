#MSH_total can be found on transcript
#current_gpa can be found on transcript
#input credit hours list as such: [4,4,3]

def calculate_required_semester_gpa(current_gpa,target_gpa,MSH_total,credit_hours_list):
    
     
    target_weight = float(target_gpa * (sum(credit_hours_list)+MSH_total))
    current_weight = float(current_gpa * MSH_total)
    return round(float(target_weight-current_weight)/sum(credit_hours_list),4)

#example required gpa calculation
print( calculate_required_semester_gpa(2.712 , 3.000 , 48 , [4,4,4,4]) )