'''

File I/O Project
Grade 12 CS
Animal Crossing Data
'''

import string
import csv


def create_list(files_list):
    item_list=[]
    item_name=[]
    
    for file in files_list:
        file_name=str(file)[:-4]
        object_type=file_name
        
        with open(file, encoding="utf8") as fileIn:
            reader=csv.DictReader(fileIn)

            for line in reader:
                name=line['\ufeffName']
                
                if name not in item_name and line['Buy']!='NFS' and line['Source']=="Nook's Cranny" and line['Color 1']!='None':
                    temp_item=[object_type,name,int(line['Buy']),int(line['Sell']),line['Color 1'], line['Color 2'],line['Tag']]
                    item_list.append(temp_item)
                    item_name.append(name)
                    
    return item_list



def calculate_lost_value(item_list):
    for item in item_list:
        original_price=item[2]
        sell_price=item[3]
        lost_value=original_price-sell_price

        item.append(lost_value)
    return item_list



#creates dictionary with type as key
def create_object_dict(item_list, object_type_dict):
    for item in item_list:
        object_type=item[0]
        
        if object_type not in object_type_dict:
            object_type_dict[object_type]={}

    return object_type_dict



#create dictionary with lost value as key
def create_lost_value_dict(item_list,object_type_dict,lost_range_list):
    for object_type in object_type_dict:
        lost_value_dict={}

        for lost_range in lost_range_list:
            #adds the keys
            min_range=lost_range[0]
            max_range=lost_range[1]
            lost_range_string=str(min_range)+" to "+str(max_range)
            lost_value_dict[lost_range_string]={}
        
        for item in item_list:
            if item[0]==object_type:
                #if type matches
                lost_val=item[7]
                object_name=item[1]
                item_data=create_object_data(item)

                for lost_range in lost_range_list:
                    #lost_range is a list
                    if lost_val>=int(lost_range[0]) and lost_val<=int(lost_range[1]):
                        lost_range_string=str(lost_range[0])+" to "+str(lost_range[1])
                        lost_value_dict[lost_range_string][object_name]=item_data
            
        object_type_dict[object_type]=lost_value_dict

    return object_type_dict



def create_object_data(item_info):
    data=[]
    
    #buy
    data.append(item_info[2])
    #sell
    data.append(item_info[3])
    #color 1
    data.append(item_info[4])
    #color 2
    data.append(item_info[5])
    #tag
    data.append(item_info[6])

    return data



def print_data(object_type_dict):
    print(f'ANIMAL CROSSING HOUSE FURNITURE ANALYSIS')
    print("{item type: {lost value when sold: {object name: [buy price, sell price, color 1 , color 2, tag]}}}")
    print(f'\n')
          
    for object_type in object_type_dict:
        print(f'{object_type.capitalize()}\n')
        
        
        lost_val_dict=object_type_dict[object_type]
        #lost val:--

        for lost_range in lost_val_dict:
            print(f'{lost_range}')
            object_data_dict=object_type_dict[object_type][lost_range]

            if bool(object_data_dict)==False:
                print("no items in range")

            for object_name in object_data_dict:
                object_data=object_data_dict[object_name]
                print(f'{object_name}: {object_data}')
                
            print(f'')
            
        print(f'\n')
                


#main
all_files=['housewares.csv','miscellaneous.csv','wall-mounted.csv']
item_list=create_list(all_files)
calculate_lost_value(item_list)

##lost_range=sort_lost(item_list)
lost_range_list=[[0,500],[501,1000],[1001,1500],[1501,2000],[2001,3000],[3001,4000],[4001,6000],[6001,15000],[15001,50000],[50001,200000]]

object_type_dict={}
create_object_dict(item_list, object_type_dict)

#changes object_type_dict
create_lost_value_dict(item_list,object_type_dict,lost_range_list)

#prints to shell
print_data(object_type_dict)
