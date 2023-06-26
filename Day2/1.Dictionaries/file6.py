# More about get

# user = {'name': 'Ayan'}
# when you wnat to return customized message other than none when key is not present
# print(user.get('fav_music', 'not found'))

# When there are two same keys in dictionary than the value of later key will override the former one


# ##########    Homerwork   #############

# Define a function that takes input n and return a dictionary containing cube of n

def cube_generate(n):
    cubes = {}
    for i in range(1, n+1):
        cubes[i] = i**3
    return cubes


ans = cube_generate(4)
print(ans)
