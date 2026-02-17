

def sample_range(lst):
    return max(lst) - min(lst)

my_list = [5,1,0,-2,9,-3,1,12]
my_range = sample_range(my_list)
print(my_range)

for i in range(len(my_list)):
    print(my_list[i])