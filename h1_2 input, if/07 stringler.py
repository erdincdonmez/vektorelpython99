a = "Ankara" # stringler bir tür dizidir.
b = "Vektörel"
c = a+b
c = f"{a} ile {b}" # f ile string formatlama
print(c)
print(f"{a} ile {b}")
c = "{} ile2 {}".format(a,b)
print(c)
c = "%s ile3 %s %d %f" %(a,b,5,3)
print(c)


print(a[0]) # index/indis hafızadaki yeri ifade eder.
print(b[2:4])
print(b[2:])
print(b[:4])
print(b[2:9:2]) # başlangıç:bitiş:atlamamiktari
print(b[-3]) # sağdan/sondan index
print(b[-3:])
print(b[:])
print(b[::-1])# terse çevirir 

meyveler = ["Muz","Dut","Nar"] #liste türü dizi
print(meyveler)
print(meyveler[2])

print(a)
print(*a)
print(*a,sep="-")
print(*a,sep="\n")
print(*a[::-1],sep="\n")
##01234
##Vektö
