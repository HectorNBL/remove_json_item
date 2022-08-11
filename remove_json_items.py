from fileinput import filename
import os,json

obj_to_del = ["name", "symbol"] #items you want to delete here.

#This is the path to the folder containing your json files
#No need to change
path_to_json = ((os.path.dirname(os.path.abspath(__file__)))+'/json/')

num_to_del = len(obj_to_del)
key = 0

def del_fun(n, k):
    while n > 0:
      try:
        key_value = obj_to_del[k]
        print(key_value)
        del data[key_value]
        print("key: " + str(k) + " remaining: " + str(n) + " item: ")
        n-=1
        k+=1
        print('Next')
      except:
        print("The item: " + str(key_value) + " doesn't exist in your file")
        n-=1
        k+=1
        continue

file_num = 1
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  print("Modifying file #" + str(file_num))
  with open(path_to_json+file_name, 'r') as f:
    data = json.load(f)
    del_fun(num_to_del, key)
  with open(path_to_json+file_name, 'w') as f:
      data = json.dump(data, f, indent=4)
  file_num+=1
print("Done!")


