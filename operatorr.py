a = 10
b = 2
print(f"{a+b}") #penjumlahan
print(f"{a-b}") #pengurangan
print(f"{a*b}") #perkalian
print(f"{a/b}") #pembagian
print(f"{a%b}") # modulus(sisa pembagi)
print(f"{a**b}") #pangkat
print(f"{a//b}") #pembagian dengan pembulatan ke bawah
b += 30 # artinya b= b+30
print(f"{b}\n") 

# operator loogika
print(f"{True and True}") # keduanya benar maka benar
print(f"{True or False}") # salah satunya benar maka benar
print(f"{not True}\n") # kebalikan 

# operatpr keanggotaan
a = [1,2,3,4,5,6]
print(f"{2 in a}") # apakah 2 ada di dalam variabel a
print(f"{1 not in a}\n") # apakah 1 tidak ada dalam vaeriabel a

#operator identitas
c = [10,11,12,13]
print(f"{c is a}")
d = [10,11,12,13] # walaupun c is d nilainya sama tetapi tempat memory nya berbeda (answer: false)
e = c
print(f"{e is c}") # karena tempat memor nya sama (answer: True)
