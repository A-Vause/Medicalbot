welcome_promt = "Welcome Doctor, what would you like to do today?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_promt = "What is the patient's name?\n"
appearance_promt = "How is the patients general appearance?\n - 1: Normal\n - 2: Irritable or lethagic\n"
eye_promt = "How are the patients eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
skin_promt = "How is the patients skin when it's pinched?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"
error_message = "Invalid entry please try again.\n"
severe_dehydration = ("Severe dehydration")
some_dehydration = ("Some dehydration")
no_dehydration = ("No dehydration")


patients_and_diagnosis = [
   "Mike- Severe dehydration",
   "Sally- No dehydration",
   "Kate- Some dehydration"
]


def list_patients():
    for patient in patients_and_diagnosis:
      print(patient)


def save_new_diagnosis(name, diagnosis):
  if name == "" or diagnosis == "":
     print(error_message)
     return    
  final_diagnosis = name + "- " + diagnosis
  patients_and_diagnosis.append(final_diagnosis)
  print("Final diagnosis:", final_diagnosis, "\n")


def asses_skin(skin):
   if skin == "1":
      return some_dehydration
   elif skin == "2":
      return severe_dehydration  
   else:
      return ""

def asses_eyes(eyes):
   if eyes == "1":
      return no_dehydration
   elif eyes == "2":
      return severe_dehydration   
   else:
      return ""
def asses_appearance():
   appearance = input(appearance_promt) 
   if appearance == "1":
      eyes = input(eye_promt)
      return asses_eyes(eyes)
   elif appearance == "2":
      skin = input(skin_promt) 
      return asses_skin(skin)    
   else:
      return ""

def start_new_diagnosis():
    name = input(name_promt)
    diagnosis = asses_appearance()
    save_new_diagnosis(name, diagnosis)



def main():
  while(True):  
    selection = input(welcome_promt)
    if selection == "1":
        list_patients()
    elif selection == "2":
        start_new_diagnosis()
    elif selection == "q":
        return


main()  

