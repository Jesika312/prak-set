aplikasi={
    1:{"A","B","D","E",'F'},
    2:{"B","D","G"},
    3:{"C","F","G"}
}
set_aplikasi=[]
for keys in aplikasi.keys():
    set_aplikasi.append(set(aplikasi[keys]))
print(set_aplikasi)
hasil=set_aplikasi[0]&set_aplikasi[1]&set_aplikasi[2]
hasil_SEMUA=set_aplikasi[0]|set_aplikasi[1]|set_aplikasi[2]
print("hasil:",hasil)
print("hasil semua:",hasil_SEMUA)