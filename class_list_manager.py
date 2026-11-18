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


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("search for Sara:", serch_name(names, "Sara"))

main()
