
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
                    idx += 1
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

        for hl_lists in range(len(self.header_list)): # 4 wheel ayrirmaq ucun
            checksum_header = 0
            dictionary_eeprom_datas = {}
            for elem_hl_inside in range(len(self.header_list[hl_lists])):  #her wheelin icini burdan baslayiram yoxlamaga
                
                checksum_header += int(self.header_list[hl_lists][elem_hl_inside])

            if checksum_header % 256 != 0:
                
                return(f"Wheel {hl_lists + 1} header checksum not correct") #adlandirmada wheel 1 olsun deye idx+1 var
            
            else:
                keys_idx = 0
                steps = 0

                for j in range(len(self.header_list[hl_lists])-1):
                    checksum = 0
                    adding_first_elem = True
                    length_check = True
                    steps = 0
                    temp_elem_for_add_dict = ""

                    regions_start = int(self.header_list[hl_lists][j]) # headerin 0ci icinde 0-ci indexdeki elem - 9 (ilk region)= temp
                    
                    regions_end = int(self.header_list[hl_lists][j+1])    # header-dən sonrakı index

                    if regions_end == 0:
                            regions_end = len(self.wheels_list[hl_lists])   # əgər 0-dırsa, axıra qədər get
                    
                    if regions_start != 0:
                        
                        for x in range(regions_start,regions_end):

                            if self.wheels_list[hl_lists][x].isdigit():
                                checksum += int(self.wheels_list[hl_lists][x])
                            
                            else:
                                checksum += ord(self.wheels_list[hl_lists][x])
                            
                            
                            if j < 2:
                            
                                if length_check == True and adding_first_elem == True and x != regions_end:
                                    temp_for_length = self.wheels_list[hl_lists][x]
                                    dilara = "KOD"
                                    
                                if adding_first_elem == False:
                                    temp_elem_for_add_dict += self.wheels_list[hl_lists][x]
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
                                    
                                
                                
                                if x == regions_end-1:
                                    
                                    dictionary_eeprom_datas.update({dictionary_keys[keys_idx]:""})
                                    temp_elem_for_add_dict = "" 
                                    adding_first_elem = True
                                    dilara = "KOD1"
                                    keys_idx += 1


                                if dilara == "KOD":
                                    adding_first_elem = False
                    
                  
                        self.eeprom_datas_list.append(dictionary_eeprom_datas.copy())

                        if checksum % 256 != 0:
                            checksum = 0
                            
                            return(f"Wheel {hl_lists + 1}, region{j + 1} cheksum not correct")
                
        return True

    def compare_wheels_elements(self):
          

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
print(eeprom.checksum())

print(eeprom.compare_wheels_elements())










