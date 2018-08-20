import re

def get_text():
  return (
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 70,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 60,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 248,80\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 248,80\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 248,80\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 248,80\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 248,80\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 248,80\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 130,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 130,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 70,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 70,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 70,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 70,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 70,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 60,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 70,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 130,00\n"
    "04/08/2018 0009570 5 209 CR 002 03/12/2018 999 3 1 padrao RJ 130,00\n"
  )
  
 
def get_user_data():
  return [[490, 7], [120, 2], [1244, 5], [520, 4], [60, 1]]


def find_occur(vector, value, i):
  temp_val = 0
  temp_arr = []
  
  for ind, val in enumerate(vector):
    if val == value / i and temp_val != value:
      temp_arr.append(ind)
      temp_val += value /i
  
  return temp_arr
  

  

def main():
  arr  = [10, 20, 20, 40, 10, 80, 20, 60, 40]
  data = get_user_data()
  text = get_text()
  match  = re.findall(r"\b[a-zA-Z]{2}\b.*\b(\d+,\d+)\b", text)
  indexs = []
  
  for i, v in enumerate(match):
    match[i] = float(v.replace(",", "."))
  
  for index, value in enumerate(data):
    result = find_occur(match, *value)
    indexs.extend(result)
    
  
  for i, v in enumerate(match):
    if i in indexs:
      print("{} OK {}{}".format("\033[92m", "\033[0m", v))
    else:
      print("{} ?? {}{}".format("\033[91m", "\033[0m", v))
 

if __name__ == "__main__": 
  main()





