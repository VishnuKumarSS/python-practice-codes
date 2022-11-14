unit = int(input("Enter the Units :"))
if (unit<=100):
    print("No need to pay")
elif(unit<=200):
    energy_charge = (unit-100)*1.5
    duty = unit/10
    fixed_charge = 20
    print("The amount to be paid is: ",energy_charge+duty+fixed_charge)
elif(unit<=500):
    energy_charge = ((unit-200)*3)+(100*2)
    duty = unit/10
    fixed_charge = 30
    print("The amount to be paid is: ",energy_charge+duty+fixed_charge)
else:
    energy_charge = ((unit-500)*6.6)+(300*4.6)+(100*3.5)
    duty = unit/10
    fixed_charge = 50
    print("The amount to be paid is: ", energy_charge+duty+fixed_charge)

