

left = int(input("Number of left shoes: "))
right = int(input("Number of right shoes: "))

pairs = min(left, right)
leftover = abs(left - right)

if left > right:
  leftover_type = 'left'
elif right > left:
  leftover_type = 'right'
else:
  leftover_type = None

if pairs == 1:
  pair_text = 'pair'
else:
  pair_text = 'pairs'

if pairs == 1:
  pairs_verb = 'is'
else:               
  pairs_verb = 'are'    

if leftover > 0:
  leftover_text = f' and {leftover} leftover {leftover_type} shoe' + ('s' if leftover > 1 else '')
else:
  leftover_text = ' no leftover shoes'

print(f'There {pairs_verb} {pairs} {pair_text}{leftover_text}.')  
