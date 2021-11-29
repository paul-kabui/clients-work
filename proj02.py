import csv
import pandas as pd
# if panda is not intalled use pip install pandas

def get_data_list(FILE_NAME):
    file = open(FILE_NAME)
    csvreader = csv.reader(file)
    data_list = []
    for row in csvreader:
        data_list.append(row)
    return data_list


def get_monthly_averages(data_list):
    data_list.pop(0)

    date = [i[0][0:10] for i in data_list]
    volume = [float(i[5]) for i in data_list]
    close = [float(i[6]) for i in data_list]

    refined_data = {'date': date,'volume':volume,'close':close}
    df = pd.DataFrame(refined_data)
    df['date'] = pd.to_datetime(df.date)
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date') 

    #calculating sales = v * c 
    #calculating total_monthly_volume = (V1 + V2 + ... + Vn)
    #calculating total_monthly_sales = (V1*C1 + V2*C2 + Vn*Cn)
    df['sales'] = df['volume'] * df['close']
    total_monthly_volume = df.volume.resample('M').sum()
    total_monthly_sales = df.sales.resample('M').sum()
    avg_whole_month = total_monthly_sales/total_monthly_volume
    avg_whole_monthList = avg_whole_month.tolist()
    
    months = [i[0][0:7] for i in data_list]
    unduplicated_months = []
    for month in months:
        if month not in unduplicated_months:
            unduplicated_months.append(month)
    unduplicated_months.reverse()
    
    monthly_avg_list = []
    for k in range(len(unduplicated_months)):
        data_tuple = float(str("{:.2f}".format(avg_whole_monthList[k]))), unduplicated_months[k],
        monthly_avg_list.append(data_tuple)

    return monthly_avg_list


def print_info(monthly_averages_list):
    monthly_averages_list.sort()
    avg_list = []
    for data in monthly_averages_list:
        dateList = data[1].split('-')
        date = dateList[1]+'-'+dateList[0]
        formated_data = date,data[0]
        avg_list.append(formated_data)
   

    l = len(avg_list)
    s = l-6
    lowest = avg_list[0:6]
    highest = avg_list[s:l]
    with open('monthly_averages.txt','w') as file:
        file.write('6 best months for Google stock: \n')
        for mon in highest:
            highest_stock = str(mon[0])+','+str(mon[1])+'\n'
            file.write(highest_stock)
        file.write('6 worst months for Google stock: \n')
        for lists in lowest:
            lowest_stock = str(lists[0])+','+str(lists[1])+'\n'
            file.write(lowest_stock)
    file.close()


FILE_NAME = 'table.csv'
data_list = get_data_list(FILE_NAME)
monthly_averages_list = get_monthly_averages(data_list)
print_info(monthly_averages_list)