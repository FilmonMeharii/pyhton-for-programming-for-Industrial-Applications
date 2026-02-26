


def count_votes(votes):
    results = {}
    for vote in votes:
        if vote in results:
            results[vote] += 1
        else:
            results[vote] = 1   
    return results

data = input("Given votes: ")
given_votes = data.split()
election_results = count_votes(given_votes)
for candidate in election_results:
    print(f"{candidate}: {election_results[candidate]} votes")