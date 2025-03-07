# def count_endangered_species(endangered_species, observed_species):
#     e_set = set(endangered_species)

#     count = 0
#     for species in observed_species: #might change to o_set
#         if species in e_set:
#             count += 1
#     return count

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  



def navigate_research_station(station_layout, observations):
    letter_to_index = {char: index for index, char in enumerate(station_layout)}
    curr_pos = letter_to_index[observations[0]] 
    total_time = curr_pos

    #print(f'{letter_to_index}')
    for observation in observations[1:]:
        next_pos = letter_to_index[observation]  
        total_time += abs(curr_pos - next_pos)  
        curr_pos = next_pos 
    
    return total_time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))