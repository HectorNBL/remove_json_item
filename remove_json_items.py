from fileinput import filename
import os,json

#Only change the content of these two:
obj_to_del = ["name", "symbol"] #items you want to delete here.
attr_to_del = [1, 2] #this will delete the first and second attributes

#This is the path to the folder containing your json files
#No need to change
path_to_json = ((os.path.dirname(os.path.abspath(__file__)))+'/json/')

num_to_del = len(obj_to_del)
num_attr_to_del = len(attr_to_del)
key = 0
attr_key = 1

def del_attributes(n, v):
  while n > 0:
    try:
      del data['attributes'][v]
      n-=1
      v+=1
      #print("n: " + str(n) + " v: " + str(v))
    except:
      print("The item: " + str(v) + " doesn't exist in your file")
      n-=1
      v+=1
      continue

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
        print("The object: " + str(key_value) + " doesn't exist in your file")
        n-=1
        k+=1
        continue

file_num = 1
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  print("Modifying file #" + str(file_num))
  with open(path_to_json+file_name, 'r') as f:
    data = json.load(f)
    del_fun(num_to_del, key)
    del_attributes(num_attr_to_del, attr_key)
  with open(path_to_json+file_name, 'w') as f:
      data = json.dump(data, f, indent=4)
  file_num+=1
print("Done!")


