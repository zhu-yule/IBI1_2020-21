# Record the student's information
first_name = input('please input the first name')
last_name = input('please input the last name')
undergraduate_programme = input('please input the undergraduate programme')

# create a class called 'Student'
class Student(object):

    # create a function within this class which prints the student’s full name and their undergraduate programme
    def __init__(self, first_name, last_name, undergraduate_programme):
        self.first_name = first_name
        self.last_name = last_name
        self.undergraduate_programme = undergraduate_programme
    print('Name:', first_name,last_name, '      undergraduate programme:', undergraduate_programme)

# an example:
# first_name = 'Yule'
# last_name = ' Zhu'
# undergraduate_programme = 'BMI'

