def write_craters(eligible_crater_list):
    with open('crater.txt', 'a') as file:
        file.write('ID\tName\tLatitude\tLongitude\tDiameter\n')
        for eligible_crater in eligible_crater_list:
            ID = str(eligible_crater[0])
            latitude = str("{:.2f}".format(eligible_crater[2]))
            longitude = str("{:.2f}".format(eligible_crater[3]))
            diameter = str("{:.2f}".format(eligible_crater[4]))
            file.write(ID+'\t'+
                        eligible_crater[1]+'\t'+
                        latitude+'\t'+longitude+'\t'+
                        diameter+'\n')
    file.close()

def get_eligible_craters(crater_list):
    eligible_craters = []
    for craters in crater_list:
        latitude = craters[2]
        longitude = craters[3]
        diameter = craters[4]
        if latitude >= -40 and latitude <=50:
            if longitude >= 40 and longitude <= 135:
                if diameter >= 60:
                    eligible_craters.append(craters)
    # print(eligible_craters)
    return eligible_craters


def get_crater_tuple(lines):
    dataList = []
    final_list = []

    for line in range(len(lines)):
        data = lines[line].split(',')
        dataList.append(data)
    del dataList[0:3]
    extracted_data_list = []
    for info in dataList:
        crater_info = info[0].replace('\t',',').split(',')
        extracted_data = (int(crater_info[0]),
                        str(crater_info[1]),
                        float(crater_info[2]),
                        float(crater_info[3]), 
                        float(crater_info[4]))
        final_list.append(extracted_data)
    return final_list

def read_crater(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines

filename = input('Enter the filename: ')
crater_data = read_crater(filename)
crater_list = get_crater_tuple(crater_data)
eligible_crater_list = get_eligible_craters(crater_list)
write_craters(eligible_crater_list)
