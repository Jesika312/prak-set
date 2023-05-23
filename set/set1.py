n=int(input("masukan nilai n:"))
bilangan_input=set()
for i in range (n):
    bilangan=int(input("masukan bilangan:"))
    bilangan_input.add(bilangan)
    bilangan
print(f"bilangan unik:{bilangan_input}")
print(f"bilangan terbesar:{max(bilangan_input)}")
print(f"bilangan terkecil:{min(bilangan_input)}")
print(f"jml bil unik:{len(bilangan_input)}")
