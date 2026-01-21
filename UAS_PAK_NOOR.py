import random

print("==== GAME TEBAK ANGKA ====")

print("Rules")
print("1. Tebak angka dari 1 sampai 100")
print("2. Kesempatan 15 kali")
print("3. Tidak ada batas waktu")
print("4. Setiap tebakan akan diberi petunjuk apakah angka terlalu ke besar atau terlalu ke kecil")
kesempatan  = 15  #

angka = random.randint(1, 100)


print("\nSaya sudah memilih angka antara 1 sampai 100")

for i in range(kesempatan):
    print(f"\nKesempatan ke-{i+1}")


    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan > angka:
        print("Angkaku lebih ke kecil")
    elif tebakan < angka:
        print("Angkaku lebih ke besar")
    else:
        print(f"Selamat, tebakan kamu BENAR!")
        break
else:
    print("\nKesempatan habis!")
    print(f"Angka yang benar adalah: {angka}")
    print("=== GAME OVER ===")
    exit()