'''numbers_list=[num for num in range(20)]
even_numbers_list=[num for num in range(24) if num%2==0]
comman_elements=set(numbers_list).intersection(even_numbers_list)#[0,2,4,6,8,10,12,14,16,18]
diff_elements=set(numbers_list)-set(even_numbers_list)
diff_elements1=set(even_numbers_list)-set(numbers_list)
print(numbers_list)
print(list(comman_elements))
print(list(diff_elements))
print(diff_elements1)
'''
US_companies=["Google","Facebook","Twitter","Instagram","Pinterest","USPolo"]
Indian_companies=["TCS","Wipro",'Infosys',"Google","Facebook","gd"]
matched_list=[com for com in Indian_companies if com in US_companies]
unmatched_list=[com for com in Indian_companies if com not in US_companies]
print(matched_list)
print(unmatched_list)