favorite_numbers = {'Jared': ['3', '32', '45'], 
        'Greg': ['10', '23', '76'], 
        'Liam': ['27', '66', '54'], 
        'Gabby': ['8', '41', '73'], 
        'Sideny': ['88', '98', '60']}

for person, numbers in favorite_numbers.items():
    numbers_list = ','.join(map(str, numbers))

    print(f"{person}'s favorite numbers are: {numbers_list}\n")