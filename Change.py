import collections

class Change(object):
  def __init__(self):
    super(Change, self).__init__()
    
    
  def makeChange(self, change):
    coinVaulues = collections.OrderedDict()
    coinVaulues['h'] = 50
    coinVaulues['q'] = 25
    coinVaulues['d'] = 10
    coinVaulues['n'] = 5
    coinVaulues['p'] = 1
    coins = {}
    for key in coinVaulues:
      while change >= coinVaulues[key]:
        coins[key] = coins.get(key, 0) + 1
        change -= coinVaulues[key]

    return coins