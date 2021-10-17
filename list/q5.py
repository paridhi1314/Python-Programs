def match(words):

  counter = 0;

  for i in words:
    if len(i) >= 2 and i[0] == i[-1]:
      counter+=1
  return counter;

print(match(['aba','2332','dddfd','fghkg']))