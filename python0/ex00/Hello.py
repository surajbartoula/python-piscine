ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")
# Tuple are immutable so need to create new one
ft_set.remove("tutu!")
# sets are unordered so there is no index
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
# tuple, string, int immutable
