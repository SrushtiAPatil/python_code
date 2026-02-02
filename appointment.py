appointments = []     
patients = set()       
slots = {}           
slot_time = ()         

n = int(input("Enter number of appointments: "))

for i in range(n):
    patient = input("Enter patient name: ")
    time = input("Enter slot time (10AM-11AM): ")

    slot_time = (time,)     

    if patient in patients:
        print("❌ Duplicate booking not allowed")
        continue

    patients.add(patient)
    slots[time] = patient
    appointments.append({"patient": patient, "slot": slot_time})

print("\n🏥 Appointment Summary")
for a in appointments:
    print("Patient:", a["patient"], "| Slot:", a["slot"][0])

print("\nTotal Unique Patients:", len(patients))
