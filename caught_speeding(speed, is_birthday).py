def caught_speeding(speed, is_birthday):
  if speed <= 60:
    return 0
  elif speed <= 80 or speed >= 61:
    return 1
  elif speed > 80:
    print(2);
  else: return speed * 5
  
