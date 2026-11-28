# Class List Manager - Group 5
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====
# Written by: Btool aleid (task 1)
def count_names(names):
    return len(names)

#Written by: Manal Alsaif(task2)
def search_name(names, name):
    for n in names:
        if n==name:
            return True 
        return False

# Written by: Elaf Alhumayzi (task 3)
def to_upper(names):
    new_names = [ ]
    for name in names:
        new_names.append(name.upper())
    return new_names

# Written by: jana aldwirij (task 3)
def sort_names(names):
    sorted_list = sorted(names)
    return sorted_list
    
# Written by: Farah Ali (task 8)

def remove_duplicates(names):

    unique_names = []

    for name in names:

        if name not in unique_names:

            unique_names.append(name)

    return unique_names

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    
    print("search for Sara:", search_name(names, "Sara"))
    print("Names in uppercase:", to_upper(names))
    print("Sorted names:", sort_names(names))
    print("Without duplicates:", remove_duplicates(names))
main()
