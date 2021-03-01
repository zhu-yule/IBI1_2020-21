# create a function to calculate the total mark for all students
def calculate(name, code, poster, exam):
    Name = name
    grade = int(code)*0.4 + int(poster)*0.3 + int(exam)*0.3
    return(Name, grade)

#encode all information
print('please input student name ')
Name = input()
print('please input student grade for the code portfolio')
Code_portfolio = input()
print('please input student grade for the poster presentation')
Poster_presentation = input()
print('please input student grade in the final exam')
Final_exam = input()

#calculate the total mark
total_mark = str(calculate(Name, Code_portfolio, Poster_presentation, Final_exam))
#unify the form
total_mark = total_mark.replace('(', '')
total_mark = total_mark.replace("'", '')
total_mark = total_mark.replace(',', '')
total_mark = total_mark.replace(')', '')
print(total_mark)