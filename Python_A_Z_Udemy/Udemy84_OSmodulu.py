import os
"""
for i in dir(os):
    if "__" not in i:
        print(i)
"""

# pwd ile bulunan dizin listeleniyor.
# ls ile bizim bulunduğumuz  dosya dizini listeleniyor.

bulundugum_dizin=os.getcwd()
print("Bulunduğum Dizin : ",bulundugum_dizin)

ev_dizini=os.path.expanduser("~")
degisen_dizin=os.chdir(ev_dizini)
print("Değiştirilen Dizin : ",degisen_dizin)

print(os.getcwd())