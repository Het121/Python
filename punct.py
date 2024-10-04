punct="! () - $ , @"
my_str="hello !! I -- am"
no_punct=""
for char in my_str:
    if char not in punct:
        no_punct=no_punct+char
print(no_punct)