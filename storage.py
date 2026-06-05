import pickle 
import os
from students import Student

def save_data(s):
    students=[] 
    file_name="stu.pkl" 
    if os.path.exists(file_name): 
        with open(file_name,"rb") as file: 
            students=pickle.load(file) 
    students.append(s) 
    with open(file_name,"wb") as file: 
        pickle.dump(students,file) 
       

    

def load_data(): 
    with open("stu.pkl" , "rb") as file: 
        data=pickle.load(file) 
    for ele in data: 
        print("----------")
        print(ele.display())
        print("----------")
############################ 
