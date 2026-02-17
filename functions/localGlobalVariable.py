

def average(lst):
  the_sum = sum(lst)
  n = len(lst)
  return the_sum / n

measurements = input('Measurements: ')
lst_data = measurements.split()
data = [float(x) for x in lst_data]
avg = average(data)
print(f'The average of the given values is {avg}')