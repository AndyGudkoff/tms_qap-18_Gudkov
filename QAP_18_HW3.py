# 1 Привести к целому типу - 1.6, 2.99
def to_int(arr):
    whole = int(arr)
    return whole


print(to_int(1.6))
print(to_int(2.99))

# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
str_my_site = "www.my_site.com#about"


def replace_sharp_by_slash(site):
    return site.replace('#', '/')


print(replace_sharp_by_slash(str_my_site))