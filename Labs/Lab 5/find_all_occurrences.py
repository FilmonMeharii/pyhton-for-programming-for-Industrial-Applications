

def find_all_positions(lst, target):
    positions = []
    for i in range(len(lst)):
        if lst[i] == target:
            positions.append(i)
    return positions        

values = [3, 3, 5, 2, 6, 5, 4, 5, 3, 2]
min_pos = find_all_positions(values, 3) # [0, 1, 8]
print(f'Positions of 3: {min_pos}')