
class EEPROM:
    def __init__(self,file_path,num_inner_wheel_list = 4,):
        self.file_path = file_path
        self.num_inner_wheel_list = num_inner_wheel_list
        self.wheels_list = [[] for _ in range(num_inner_wheel_list)]
        

        try:
            with open (self.file_path,"r") as file:
                content = file.read()
                content = content.replace("\n", " $ ")
      
        except FileNotFoundError:
            print("Error: The specified file was not found.")
        
        
        
        content_elem = ""
        count_for_split_wheel = 0
        idx = 0
        
        for elem in content:
            if elem != " ":

                content_elem += elem

            if elem == " " and content_elem != "" and content_elem != "$":
                self.wheels_list[idx].append(content_elem)
                count_for_split_wheel = 0
                content_elem = ""
                

            elif content_elem == "$":
                
                count_for_split_wheel += 1
                content_elem = ""
                
                if count_for_split_wheel >= 2:
                    idx +=1
                    count_for_split_wheel = 0
        self.wheels_list[idx].append(content_elem)

        self.header_list = [inner[:9] for inner in self.wheels_list]
        
        print(self.wheels_list)
        #print(self.header_list)
        

    
    def checksum (self):

        header_check = False
        checksum = 0
        temp_elem_for_add_dict = ""
        dictionary_eeprom_datas = {}
        dictionary_keys = ["date", "name", "city", "country", "trayID", "partID"]

        for i in range(len(self.header_list)):
            for elem_idx in range(len(self.header_list[i])):
                
                checksum += int(self.wheels_list[i][elem_idx])

            if checksum % 256 == 0:
                header_check = True
                keys_idx = 0
                steps = 0

                for j in range(len(self.header_list)):
                    temp = int(self.header_list[i][j]) # headerin 0ci icinde 0-ci indexdeki elem - 9 (ilk region)= temp

                    for x in range(temp+1,len(self.wheels_list[i])):
                        temp_elem_for_add_dict += self.wheels_list[i][x]
                        steps += 1

                        if steps == int(self.wheels_list[i][temp]):
                            dictionary_eeprom_datas.update({dictionary_keys[keys_idx]:temp_elem_for_add_dict})
                            keys_idx += 1
                            temp_elem_for_add_dict = ""
                            steps = 0
                            break

            print(dictionary_eeprom_datas)
        




        


eeprom = EEPROM("/Users/dilara/Desktop/Dilara/Assignment1/colleague-file.log")
#print(eeprom)
eeprom.checksum()






# checksum = 0
# region_idx_list = []
# for i in range(len(wheels_list)):
#     for elem_idx in range(len(wheels_list[i])):
#         if elem_idx <=8:
#             region_idx_list.append(wheels_list[i][elem_idx])
            
# print(wheels_list)



