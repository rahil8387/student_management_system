from students import Student 
from storage import load_data,save_data 
import pickle 

def menu(): 
    while True:
        "Choose Your Options" 
        options=input('''
                        1.Press 1 for adding data 
                        2.Press 2 for load data
                        3.Press 3 for exit''')  
        if options=="1": 
            name=input("Enter Your Name:") 
            marks=int(input("Enter Your marks:")) 
            rollno=input("Enter your roll number:")
            s1=Student(name,rollno,marks) 
            save_data(s1) 
        elif options=="2": 
            print(load_data()) 
        else:
            break  
if __name__=="__main__":
    menu()

