# Class List Manager - Group 2
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Anoud", "Jood", "Sadeem", "Rana", "Rand", "Sadeem"]


#  Each student adds her function BELOW this line
# Written by: Alanoud Altammami
def count_names(names):
  return len(names)

# Written by: Sadeem Alotaibi
def search_name(names, name):
    for student in names:
        if student == name:
            return True
    return False
  # Written by: Rand Almuhaythif
def sort_names(names):
  return sorted(names)

def main():
 print("Welcome to the Class List Manager!")
 print("Class list:", names)
 print("Sorted names:", sort_names(names))

# Each student calls her function here, for example:
 print("Number of names:", count_names(names))
 print("Search for Sadeem:", search_name(names, "Sadeem"))

main()
