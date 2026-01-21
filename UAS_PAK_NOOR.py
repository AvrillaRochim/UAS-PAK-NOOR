import random

def game_tebak_angka():
    print("=== Game Tebak Angka ===")
    print("Komputer sudah memilih angka antara 1 sampai 100.")
    print("Coba tebak!")

    # Komputer memilih angka acak
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Masukkan angka yang valid ya!")

# Jalankan game
game_tebak_angka()