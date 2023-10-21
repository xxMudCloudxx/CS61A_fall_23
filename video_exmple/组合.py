def search(query, ranking = lambda r : -r.stars):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)

def reviewed_both(r, s):
    # return len([x for x in r.reviewers if x == s.reviewers])
    return fast_overlap(r.reviewers, s.reviewers)

def fast_overlap(s, t):
    i,j, count = 0, 0, 0
    while i < len(s) and j < len(t) :
        if s[i] == t[j]:
            count, i, j = count + 1, i+1, i+1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count

class Restaurant:
    all = []
    def __init__(self, name ,stars, reviewers):
        self.name, self.stars = name, stars
        Restaurant.all.append(self)
        self.reviewers = reviewers
    def similar(self, k, similarity = reviewed_both):
            others = list(Restaurant.all)
            others.remove(self)
            return sorted(others, key= lambda x : -similarity(x, self))[:k]
    
    def __repr__(self):
         return '<' + self.name + '>'

import json
reviewers_for_restaurant = {}
for line in open('reviews.json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz] = [r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])

for line in open('restaurants.json'):
    r = json.loads(line)
    reviewers = reviewers_for_restaurant[r['business_id']]
    Restaurant(r['name'], r['stars'], reviewers)

while True:
    print('>', end = ' ')
    results = search('Thai')
    for r in results:
        print(r,"is similar to", r.similar(3))