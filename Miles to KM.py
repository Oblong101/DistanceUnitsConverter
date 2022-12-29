x = input("Km to M(KTM) or M to Km(MTK)? ")
if x == "KTM":
    km1 = float(input("Input the distance in Km: "))
    miles1 = km1*1.609
    print(km1, "in miles is", miles1)

if x == "MTK":
    miles2 = float(input("Input the distance in M: "))
    km2 = miles2*0.609
    print(miles2, "in Km is", km2)

else:
    print("Error. Calculation must be either MTK(miles to kilometres) or KTM(kilometres to miles)")