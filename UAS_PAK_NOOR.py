import random

print("==== GAME TEBAK ANGKA ====")

while True:
    print("Rules")
    print("1. Tebak angka dari 1 sampai 100")
    print("2. Kesempatan 10 kali")
    print("3. Tidak ada batas waktu")
    print("4. Setiap tebakan akan diberi petunjuk apakah angka terlalu ke besar atau terlalu ke kecil")
    kesempatan  = 10  #

    angka = random.randint(1, 100)


    print("\nSaya sudah memilih angka antara 1 sampai 100")

    while kesempatan > 0:
            try:
                tebakan = int(input("Masukkan tebakan kamu: "))
            except ValueError:
                print("Harap Isi nominal yang benar")
                continue

            if tebakan > angka:
                print("Angkaku lebih ke kecil")
                kesempatan -=1
            elif tebakan < angka:
                print("Angkaku lebih ke besar")
                kesempatan -=1
            else:
                print(f"Selamat jawaban kamu benar {angka}")
                break
    else:
        print("\nKesempatan habis!")
        print(f"Angka yang benar adalah: {angka}")
        print("=== GAME OVER ===")

    ulang = input("\nApakah anda ingin mengulang? (y/n)")
    if ulang != 'y':
     print("terimakasih telah bermain")
     break