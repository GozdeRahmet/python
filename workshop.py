vize = input("vize notu:")
final = input("final notu:")

vize = float (vize)
final = float (final)
sonucNotu = vize * 0.4 + final * 0.6
print(sonucNotu)

if sonucNotu>=0 and sonucNotu<=49:
    print ("FF")

elif sonucNotu>=50 and sonucNotu<=59:
    print ("DD")
elif sonucNotu>=60 and sonucNotu<=69:
    print ("CC")
elif sonucNotu>=70 and sonucNotu<=79:
    print ("BB")
elif sonucNotu>=80 and sonucNotu<=100:
    print ("AA")
else:
    print("gecersiz ifade")
