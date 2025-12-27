import re

def check_name(name):
  pattern = r"[A-Z]+[a-z]+[^A-Za-z0-9]+"
  result = re.match(pattern, name)
  if result:
    return True
  else:
    raise ValueError("Name should contain at least One Capital, One small and One special character")

def main(): 
  try:  
    check_name()
  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()
  
