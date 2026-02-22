

def read_scores(results):
    while True:
        name = input('Name: ') # read a name
        if name == '': # if no name given
            return # quit
        score = int(input('Score: ')) # read a score
        if name in results: # if name already exists
            results[name].append(score) # add to list of scores
        else:
            results[name] = [score]