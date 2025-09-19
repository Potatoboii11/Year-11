pet_name = ['Foxy', 'Kevin', 'Donald']
pet_species = ['Dog', 'Hamster', 'Cat']
pet_age = [8,2,11]
pet_vaccination_status = [False, True, False]

pet_name.append("Hootie")
pet_species.append("blowfish")
pet_age.append(34)
pet_vaccination_status.append(True)

ind = pet_name.index('Foxy')
pet_name.remove('Foxy')
pet_species.remove(pet_species[ind])
pet_age.remove(pet_age[ind])
pet_vaccination_status.remove(pet_vaccination_status[ind])

for i in range (len(pet_name)): 
    print("Pet name:",pet_name[i])
    print("Pet Species:",pet_species[i])
    print("Pet_age:",pet_age[i])
    if pet_vaccination_status[i] == False:
        pet_vaccination_status[i] = True #Vaccinates unvaccinated animals
    print("Pet vaccination status:",pet_vaccination_status[i])
    print('')



