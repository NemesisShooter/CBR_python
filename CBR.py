import random
import itertools
import time
import sys

#1 = ON
#0 = OFF
######################################
pc_system_solve = {
"case_1" : {"case" : " EXDISPLAY Corsair Crystal Series 570X RGB Gaming Case ", "PSU state" : 1, "Motherboard state" : 1, "RAM state" : 1, "HDD state" : 0, "OS state" : 0, "Solution 1" : "Check SATA connection.", "Solution 2": "Replace HDD."},
"case_2" : {"case" : " Be Quiet Dark Base Pro 900 Black ATX Case ", "PSU state" : 0, "Motherboard state" : 0, "RAM state" : 0, "HDD state" : 0,"OS state" : 0, "Solution 1" : "Check connection between PSU and motherboard.", "Solution 2": "Replace PSU."},
"case_3" : {"case" : " Rosewill Cullinan ", "PSU state" : 1, "Motherboard state" : 0, "RAM state" : 0, "HDD state" : 0,"OS state" : 0, "Solution 1" : "Check connection with motherboard", "Solution 2": "Replace Motherboard"},
"case_4" : {"case" : " Fractal Design Define R5 ", "PSU state" : 1, "Motherboard state" : 1, "RAM state" : 0, "HDD state" : 0,"OS state" : 0, "Solution 1" : "Check connection between motherboard and RAM, HDD", "Solution 2": "Replace RAM and HDD, if this will not help replace motherboard"},
"case_5" : {"case" : " Riotoro CR1080 ", "PSU state" : 1, "Motherboard state" : 1, "RAM state" : 1, "HDD state" : 1,"OS state" : 1, "Solution 1" : "Everything is working", "Solution 2" : "But everything is working"},
"case_6" : {"case" : " Cooler Master MasterCase Pro 5 ", "PSU state" : 1, "Motherboard state" : 1, "RAM state" : 0, "HDD state" : 1,"OS state" : 0, "Solution 1" : "Check connection between Motherboard and RAM", "Solution 2": "Replace RAM"}}
print ("Cases that will be used to find solution(s)")
for case_number in pc_system_solve:
    print ("\n")
    print (case_number,"\n")
    for case in pc_system_solve[case_number]:
        print (case,':', pc_system_solve [case_number][case])
######################################

#creating random problem
######################################
case = ["Riotoro CR1080",  "Fractal Design Define R5", "Cougar QBX", "Cooler Master MasterCase Pro 5", "Rosewill Cullinan"]
case_rand = random.choice(case)
p = random.randint(0, 1)
if   p == 0:
     m = 0
elif p == 1:
     m = random.randint(0, 1)

if   m == 0:
     r = 0
     h = 0
     os = 0
elif m == 1:
     r = random.randint(0, 1)
     h = random.randint(0, 1)
     
if   r == 0 or h == 0:
     os = 0
if   r == 1 and h == 1:
     os = 1

problem = ["Case", case_rand, "PSU state", p, "Motherboard state", m, "RAM state", r, "HDD state", h, "OS state", os]
pc_system_problem = dict(itertools.zip_longest(*[iter(problem)] * 2, fillvalue=""))

print ("\n\nFOR CHECK")
for case in pc_system_problem:
    print (case,':', pc_system_problem[case])
print ("\n\nHARDWARE STATE")
#######################################

#Function to check for broken hardware in the dictionary
#######################################
def if_problem(name):
      if   name == 0:
           name = 0
      elif name == 1:
           name = 1
      return name
#######################################

#Function to print state of problematic hardware
#######################################
def if_state_printer(name):
      if   name == 0:
           name = "OFF"
      elif name == 1:
           name = "ON"
      return name
#######################################

#figuring out the state of PSU and declaring function to store information about state
#######################################
def PSU():
 for key, PSU in pc_system_problem.items():
    if key == "PSU state":
      if_problem(PSU)
      return PSU
    
psu_problem = PSU()
print ("PSU state is", if_state_printer(psu_problem))
#######################################

#figuring out the state of Motherboard and declaring function to store information about state
#######################################
def MOB():
 for key, MOB in pc_system_problem.items():
    if key == "Motherboard state":
      if_problem(MOB)
      return MOB
    
mob_problem = MOB()
print ("Motherboard state is", if_state_printer(mob_problem))
#######################################

#figuring out the state of RAM and declaring function to store information about state
#######################################
def RAM():
 for key, RAM in pc_system_problem.items():
    if key == "RAM state":
      if_problem(RAM)
      return RAM
    
ram_problem = RAM()
print ("RAM state is", if_state_printer(ram_problem))
#######################################

#figuring out the state of HDD and declaring function to store information about state
#######################################
def HDD():
 for key, HDD in pc_system_problem.items():
    if key == "HDD state":
      if_problem(HDD)
      return HDD
    
hdd_problem = HDD()
print ("HDD state is", if_state_printer(hdd_problem))
#######################################

#figuring out the state of OS and declaring function to store information about state
#######################################
def OS():
 for key, OS in pc_system_problem.items():
    if key == "OS state":
      if_problem(OS)
      return OS
    
os_problem = OS()
print ("OS state is", if_state_printer(os_problem))
#######################################

print("\n")

#Declaring str values for further use
#######################################
psu = "PSU state"
mob = "Motherboard state"
ram = "RAM state"
hdd = "HDD state"
os = "OS state"
solution1 = "Solution 1"
solution2 = "Solution 2"
#######################################

#Function for printing
#######################################
def print_function(print_1):
    print(print_1)
    time.sleep(3)
    sys.exit()
#######################################

#Algorithm to compare dictionaries and print solutions
#######################################
for key_case_s, value_case_s in pc_system_solve.items():
    for key_z, value_z in value_case_s.items():
        if psu == key_z:
            if psu_problem == value_z:
                for key_z_mob, value_z_mob in value_case_s.items():
                    if mob == key_z_mob:
                        if mob_problem == value_z_mob:
                            for key_z_ram, value_z_ram in value_case_s.items():
                                if ram == key_z_ram:
                                    if ram_problem == value_z_ram:
                                        for key_z_hdd, value_z_hdd in value_case_s.items():
                                            if hdd == key_z_hdd:
                                                if hdd_problem == value_z_hdd:
                                                    for key_z_os, value_z_os in value_case_s.items():
                                                        if os == key_z_os:
                                                            if os_problem == value_z_os:
                                                                for key_z_solution, value_z_solution in value_case_s.items():
                                                                    if solution1 == key_z_solution:
                                                                        print (key_case_s, "\nSolution: ", value_z_solution)
                                                                        check_input = str(input("\nDid it help? (Y/N): "))
                                                                        if check_input == "Y":
                                                                                print_function("Awesome, GOOD LUCK!")
                                                                        elif check_input == "N":
                                                                                for key_z_solution, value_z_solution in value_case_s.items():
                                                                                    if solution2 == key_z_solution:
                                                                                        print ("\nSolution: ", value_z_solution)
                                                                                        check_input = str(input("\nDid it help? (Y/N): "))
                                                                                        if check_input == "Y":
                                                                                            print_function("Awesome, GOOD LUCK!")
                                                                                        elif check_input == "N":
                                                                                            print_function("\nSorry but there are no more solutions, GOOD LUCK!")
#######################################
