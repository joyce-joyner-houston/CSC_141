def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')

print(user_profile)

#My Profile
my_profile = build_profile ('Bob', 'Jackson', age = 30, 
                            location = 'Philadelphia',
                            field = 'biology')