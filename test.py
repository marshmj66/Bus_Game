def permutations(string):
  if len(string) == 1:
      return set(string)
  first = string[0]
  print('first',first)
  rest = permutations(string[1:])
  print(rest)
  result = set()
  for i in range(0, len(string)):
    for p in rest:
      result.add(p[0:i] + first + p[i:])
      print('results', result)
  return result

a = permutations('aabb')
print(a)

t = 'b'
print(t[0:1])