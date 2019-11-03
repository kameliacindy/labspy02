print("Mencari nilai terbesar dari 3 bilangan..."
      "\nKetiga bilangan harus bernilai integer!"
      "\nSilahkan masukan bilangan...")

Bil1 = int(input("Masukan Bilangan 1 = "))
Bil2 = int(input("Masukan Bilangan 2 = "))
Bil3 = int(input("Masukan Bilangan 3 = "))
print("\n")

# Mencari 1 Bilangan terbesar
if (Bil1 > Bil2) and (Bil1 > Bil3):
    Terbesar = Bil1
    Nam_Bil = "Bilangan 1"
elif (Bil2 > Bil1) and (Bil2 > Bil3):
    Terbesar = Bil2
    Nam_Bil = "Bilangan 2"
elif (Bil3 > Bil1) and (Bil3 > Bil2):
    Terbesar = Bil3
    Nam_Bil = "Bilangan 3"

# Mencari 2 Bilangan terbesar
elif (Bil1 == Bil2) and (Bil1 != Bil3):
    Terbesar = Bil1
    Nam_Bil = "Bilangan 1 dan Bilangan 2"
elif (Bil1 == Bil3) and (Bil1 != Bil2):
    Terbesar = Bil3
    Nam_Bil = "Bilangan 1 dan Bilangan 3"
elif (Bil2 == Bil3) and (Bil2 != Bil1):
    Terbesar = Bil2
    Nam_Bil = "Bilangan 2 dan Bilangan 3"

print("Bilangan yang terbesar adalah", Nam_Bil, "dengan nilai", Terbesar)