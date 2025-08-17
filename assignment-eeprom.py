try:
    with open ("/Users/dilara/Desktop/Dilara/Assignment1/colleague-file.log","r") as file:
        content = file.read()
        #print(content)

except FileNotFoundError:
    print("Error: The specified file was not found.")


content = content.replace('\n',' ')
    
#number_str_list = ["0","1","2","3","4","5","6","7","8","9"]

# Stringi sadece liste cevirdik
content_elem = ""
content_list = []


for elem in content:
    
    if elem != " " :

        content_elem += elem
    

    if elem == " " and content_elem != "":
       content_list.append(content_elem)
       content_elem = ""

content_list.append(content_elem)        

print(content_list)
# liste cevirme bitdi!


# num_inner_wheel_list = 4
# wheels_list = [[] for _ in range(num_inner_wheel_list)]
# wheel_list_idx = 0
# wheel_size_counter = 9
# checksum = 0

# for idx in range(len(content_list)):
#     if idx < wheel_size_counter-1:
#         wheel_size_counter += int(content_list[idx])
        
#     elif idx <= wheel_size_counter:
#         wheels_list.insert(wheel_list_idx,content[idx])
    
#     wheel_list_idx +=1
    

# print(wheels_list)
    
