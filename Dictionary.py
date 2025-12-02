UnitedNations={
    "India":"New Delhi",
    "Afganistan":"Kabul",
    "Kiribati":"Banana",
    "Australia":"Cranberra",
    "Vatican City":"Vatican city",
    "Suadi Arabia":"Riyadh",
    "Sri lanka":"Colombo",
    "Bangladesh":"Dhaka",
    



}
#Adding Things(Values)
UnitedNations["Balochistan"]="Karachi"
print(UnitedNations)
UnitedNations["Balochistan"]="Quetta"
print(UnitedNations)
#Checking for Membership
if "India" in UnitedNations:
    print("Country Recognized by all 193 Soverign Nations")
else:
    print("Country not Recognized by all 193 Soverign Nations")

#deleting items
del UnitedNations["Vatican City"]
print(UnitedNations)

#Itrating Over The Keys
for country in UnitedNations.keys():
    print(UnitedNations[country])