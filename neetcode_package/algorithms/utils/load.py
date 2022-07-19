
def load_numbers(file_name):
    numbers =[]
    with open(file_name) as file:
        for line in file:
            numbers.append(int(line))
    return numbers

def load_strings(file_name):
  strings = []
  with open(file_name) as f:
    for line in f:
      strings.append(line.rstrip())
  return strings
