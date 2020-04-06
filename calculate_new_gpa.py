#MSH_total can be found on transcript
#current_gpa can be found on transcript
#input credit hours list and grades list as such: [4,4,3], ['A','B-','C']

def calculate_new_gpa(current_gpa,MSH_total,credit_hours_list,grades_list):
    grade_weights = {'A':4.0,
                 'A-':3.7,
                 'B+':3.3,
                 'B':3.0,
                 'B-':2.7,
                 'C+':2.3,
                 'C':2.0,
                 'C-':1.7,
                 'D+':1.3,
                 'D':1.0,
                 'D-':0.7,
                 'E':0.0}
    if( len(credit_hours_list) != len(grades_list) ):
       return ("Credit hours list must be same size as grades list")

    sem_total = 0
    for i in range(0,len(grades_list)):
        sem_total += (grade_weights[grades_list[i]]*credit_hours_list[i])
        
    cumul_total = current_gpa * MSH_total
    total_weights = cumul_total + sem_total
    total_creds = MSH_total + sum(credit_hours_list)
    new_gpa = total_weights/total_creds
    
    return round(new_gpa,3)


#example new gpa calculation:
print( calculate_new_gpa(2.712 , 48 , [4,4,3] , ['A','A','A'] ) )
