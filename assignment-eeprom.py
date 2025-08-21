
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
        
        #print(self.wheels_list)
       

    def checksum (self):


        checksum_check = False
        length_check = True
        adding_first_elem = True
        checksum = 0
        checksum_header = 0
        dilara = 'KOD'
        temp_elem_for_add_dict = ""
        dictionary_eeprom_datas = {}
        self.eeprom_datas_list =[]
        dictionary_keys = ["date", "name", "city", "country", "region_end_sum1","trayID", "partID","region_end_sum2"]

        for i in range(len(self.header_list)): # 4 wheel ayrirmaq ucun
            
            for elem_idx in range(len(self.header_list[i])):  #her wheelin icini burdan baslayiram yoxlamaga
                
                checksum_header += int(self.wheels_list[i][elem_idx])

            if checksum_header % 256 == 0:
                checksum_check = True
                keys_idx = 0
                steps = 0

                for j in range(len(self.header_list[i])-1):

                    regions_start = int(self.header_list[i][j]) # headerin 0ci icinde 0-ci indexdeki elem - 9 (ilk region)= temp
                
                    regions_end = int(self.header_list[i][j+1])    # header-dən sonrakı index

                    if regions_end == 0:
                        regions_end = len(self.wheels_list[i])   # əgər 0-dırsa, axıra qədər get

                
                    

                        for x in range(regions_start,regions_end):

                            if self.wheels_list[i][x].isdigit():
                                checksum += int(self.wheels_list[i][x])
                            
                            else:
                                checksum += ord(self.wheels_list[i][x])
                            
                            
                            if j < 2:
                            
                                if length_check == True and adding_first_elem == True:
                                    temp_for_length = self.wheels_list[i][x]
                                    dilara = "KOD"
                                    
                                if adding_first_elem == False:
                                    temp_elem_for_add_dict += self.wheels_list[i][x]
                                    steps += 1
                                    length_check = False

                                if steps == int(temp_for_length):
                                    dictionary_eeprom_datas.update({dictionary_keys[keys_idx]:temp_elem_for_add_dict})
                                    keys_idx += 1
                                    temp_elem_for_add_dict = ""
                                    steps = 0
                                    length_check = True
                                    adding_first_elem = True
                                    dilara = "KOD1"
                                    
                                
                                
                                if x+1 == regions_end:
                                    
                                    dictionary_eeprom_datas.update({dictionary_keys[keys_idx]:temp_for_length})
                                    temp_elem_for_add_dict = "" 
                                    adding_first_elem = True
                                    dilara = "KOD1"
                                    keys_idx += 1


                                if dilara == "KOD":
                                    adding_first_elem = False

                        if checksum % 256 == 0:
                            checksum_check = True
                            checksum = 0
                        else:
                            return(f"Wheel {i+1}, region{j+1} cheksum not correct")
                            
            
                self.eeprom_datas_list.append(dictionary_eeprom_datas)

            else:
                return(f"Wheel{i+1} header checksum not correct")
                
        return checksum_check
    


    def compare_wheels_elements(self,eeprom_datas_list):
          

        keys_to_check = ["date", "city", "country", "partID"]
        all_same = True  

        reference = self.eeprom_datas_list[0]
        #first_trayid = int(reference.get("trayID"))

        for dict_item in self.eeprom_datas_list:
            for key in keys_to_check:
                if dict_item.get(key) != reference.get(key):
                    all_same = False
                    break  
            
            
        if all_same:
            return True
        else:
            return False
        




        


eeprom = EEPROM("/Users/dilara/Desktop/Dilara/Assignment1/colleague-file.log")
eeprom.checksum()
print(eeprom.compare_wheels_elements(eeprom.eeprom_datas_list))










