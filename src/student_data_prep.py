import numpy as np
import pandas as pd
from os import getcwd

# M191 Student Data

student_names = ['Matthew Lin', 'David Recendiz', 'Erick Tejeda', 'Bill Cheng', 'Angelina Chen', 'Jessica De La Torre', 'Gordon Li', 'Max Fukuhara', 'Vishwanath Durgam', 'Ana Ruiz', 'Yasmeen Soriano', 'Scott Phu', 'Justin Wang', 'Roger Kave', 'Conner Gossman', 'Aaron Hofman', 'Lucas Jones', 'Rachel Qu', 'Akshata Chettupalli', 'Brandon Lin', 'Wasi Khan', 'Ahmet Gundogdu', 'Jonathan Haile', 'Edwin Shum']
student_grades = [10, 12, 12, 11, 9, 12, 10, 10, 11, 11, 12, 11, 11, 10, 11, 12, 10, 12, 9, 11, 10, 10, 12, 11]
school_names = ['None', 'None', 'None', 'Arcadia High School', 'Chaminade College Prep', 'South Gate High School', 'Rowland High School', 'Arnold O Beckman High School', 'North Hollywood High School', 'South Gate Senior High School', 'South Gate Senior High School', 'Arcadia High School', 'None', 'North Hollywood High School', 'Highland Hall Waldorf School', 'None', 'Arnold O Beckman High School', 'Diamond Bar High School', 'North Hollywood High School', 'Irvine High School', 'Tustin High School', 'University High School', 'Aveson Global Leadership Academy', 'None']

student_dict = {'Student Name': student_names, 'Grade Level': student_grades, 'School Name': school_names}

df = pd.DataFrame.from_dict(student_dict)

csv_path = getcwd() + "/data"

df.to_csv(f"{csv_path}/M191_student_data.csv", index=False)

# M196 Student Data

student_names = ['Vivian Tran', 'Rachel Qu', 'Daosiri Rattanamansuang', 'Erick Tejeda', 'Brandon Lin', 'Edwin Shum', 'Bill Cheng', 'Scott Phu', 'Justin Wang', 'Rosemany Ting', 'Anoushka Bhat', 'Nikolay Petrushin', 'Aaron Hofman']
student_grades = [12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 9, 12]
school_names = ['None', 'Diamond Bar High School', 'Granada Hills Charter High School', 'None', 'Irvine High School', 'None', 'Arcadia High School', 'Arcadia High School', 'None', 'Arcadia High School', 'Diamond Bar High School', 'Northwood High School', 'None']

student_dict = {'Student Name': student_names, 'Grade Level': student_grades, 'School Name': school_names}

df = pd.DataFrame.from_dict(student_dict)

df.to_csv(f"{csv_path}/M196_student_data.csv", index=False)
