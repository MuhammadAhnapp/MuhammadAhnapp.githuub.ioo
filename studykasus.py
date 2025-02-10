# penggunaan library
import random
fans_MU_position = random.randint( 1, 4)
# pembukaan game
print("**************************")
print("* WELCOME FOR NEW GAME *")
print("**************************")
# membuat input nama
nama_user = input("Masukkan Nama kamu : ")
#buat goa dan ubah menjadi array suapya bisa dimanipulasi
bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] *4 #goa kosong, yang sudah dibuat menjaadi array dengan []
goa_kosong_tanpakutip = " " .join (map(str, goa_kosong))

goa = goa_kosong.copy()#meng copy goa_kosong ke dalam goa, lalu diubah nilainya menadi emot  
goa[fans_MU_position -1]  = "|0_0|" 


# awal dari permainan
print(f'''\nHallo {nama_user} coba perhatikan goa dibawah ini!\n{goa_kosong_tanpakutip}''')

jawaban_user = int(input("\nMenurut kamu di goa nomor berapa FANS MU berada? [1 / 2 / 3 / 4]: "))
pertanyaan = input(f"Apakah kamu yakin dengan jawaban tersebut {jawaban_user}? [y/n]: ")

if pertanyaan == "n":
  print("Program selesai, Silahkan mulai program dari awal ")
  exit()
elif pertanyaan == "y":
  if  jawaban_user == fans_MU_position:
    print(f'{goa}\nSELAMAT {nama_user} KAMU MENANG, ')
  else:
    print(f'{goa}\nKAMU KALAH FANS MU bukan berada di posisi itu')
else:
  print("Silahkan Ketikkan [y/n] ")
  exit()