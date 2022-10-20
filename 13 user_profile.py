def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie informacje
    o użytkowniku"""
    user_info ['first_name'] = first
    user_info ['last_name'] = last
    return user_info

user_profile = build_profile ('albert', 'eintstein', 
                            location='princeton',
                            field = 'fizyka')                              
print (user_profile)

my_profile = build_profile( 'Dominik','Maciazek', work = 'musican', python = 'początkujący')

print (my_profile) 
