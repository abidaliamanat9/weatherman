import os
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m' 
class WeatherDataProcessor:


    months = ["January", "February", "March", "April", "May", "June", "July", "August",
                            "September", "October", "November", "December"]
    month_names = ["Jan.txt", "Feb.txt", "Mar.txt", "Apr.txt", "May.txt", "Jun.txt", "Jul.txt", "Aug.txt",
                            "Sep.txt", "Oct.txt", "Nov.txt", "Dec.txt"]

    def processYearData(self, year_folder_path):
        inputs = year_folder_path.split()
        city = inputs[1].split('/')
        max_temp_dic = dict()
        max_humi_dic = dict()
        min_temp_dic = dict() 
        i = 0
        while i < 12:
            file_name = city[4]+"_"+inputs[0]+"_"+WeatherDataProcessor.month_names[i]
            file_path = os.path.join(inputs[1],file_name)
            try:
                if os.path.exists(file_path):
                    file = open(file_path, 'r')
                    lines = file.readlines()[1:]
                    for line in lines:
                        line = line.split(',')
                        if len(line) > 1 and line[0] != 'PKT':
                            if line[1] != '':
                                max_temp_dic[line[0]] = line[1]
                            if line[7] != '':
                                max_humi_dic[line[0]] = line[7]
                            if line[3] != '':
                                min_temp_dic[line[0]] = line[3]
                i+=1
            except:
                continue       
        max_temp = max(max_temp_dic, key=max_temp_dic.get)
        dates = max_temp.split('-')
        print(f"Maximum: {max_temp_dic[max_temp]}C on {WeatherDataProcessor.months[int(dates[1])-1]} {dates[2]}")

        min_temp = min(min_temp_dic, key=min_temp_dic.get)
        dates = min_temp.split('-')
        print(f"Minimum: {min_temp_dic[min_temp]}C on {WeatherDataProcessor.months[int(dates[1])-1]} {dates[2]}")

        max_humi = max(max_humi_dic, key=max_humi_dic.get)
        dates = max_humi.split('-')
        print(f"Maximum: {max_humi_dic[max_humi]}% on {WeatherDataProcessor.months[int(dates[1])-1]} {dates[2]}")

    def processMonthAverage(self, year_folder_path):
        inputs = year_folder_path.split()
        input1s = inputs[0].split('/')
        city = inputs[1].split('/')
        max_temp_dic = dict()
        avg_humi_dic = dict()
        min_temp_dic = dict()

        file_name = city[4]+"_"+input1s[0]+"_"+WeatherDataProcessor.month_names[int(input1s[1])-1]
        file_path = os.path.join(inputs[1],file_name)
        try:
            if os.path.exists(file_path):
                file = open(file_path, 'r')
                lines = file.readlines()[1:]
                for line in lines:
                    line = line.split(',')
                    if len(line) > 1 and line[0] != 'PKT':
                        if line[1] != '':
                            max_temp_dic[line[0]] = int(line[1])
                        if line[7] != '':
                            avg_humi_dic[line[0]] = int(line[8])
                        if line[3] != '':
                            min_temp_dic[line[0]] = int(line[3])
        except:
            print("No such file exist")
        max_temp = max_temp_dic.values()
        if max_temp:
            avg_max_temp = int(sum(max_temp)/len(max_temp))
            print(f"Highest Average: {avg_max_temp}C")
        min_temp = min_temp_dic.values()
        if min_temp:
            avg_min_temp = int(sum(min_temp)/len(min_temp))
            print(f"Lowest Average: {avg_min_temp}C")
        all_avg_humi = avg_humi_dic.values()
        if all_avg_humi:
            avg_humi = int(sum(all_avg_humi)/len(all_avg_humi))
            print(f"Average Humidity: {avg_humi}%")
    
    def processMonthPrint(self, year_folder_path):
        inputs = year_folder_path.split()
        input1s = inputs[0].split('/')
        city = inputs[1].split('/')

        file_name = city[4]+"_"+input1s[0]+"_"+WeatherDataProcessor.month_names[int(input1s[1])-1]
        file_path = os.path.join(inputs[1],file_name)
        try:
            if os.path.exists(file_path):
                file = open(file_path, 'r')
                lines = file.readlines()[1:]
                red_plus = RED + '+' + RESET
                blue_plus = BLUE + '+' + RESET
                print(f"{WeatherDataProcessor.months[int(input1s[1])-1]} {input1s[0]}")
                for line in lines:
                    line = line.split(',')
                    if len(line) > 1 and line[0] != 'PKT':
                        dline = line[0].split('-')
                        if line[1] != '':
                            print(f"{dline[2]}{RED}{' '.join([red_plus] * int(line[1]))}{RESET} {int(line[1])}C")
                            # max_temp_dic[line[0]] = int(line[1])
                        if line[3] != '':
                            print(f"{dline[2]}{BLUE}{' '.join([blue_plus] * int(line[3]))}{RESET} {int(line[3])}C")
                            # min_temp_dic[line[0]] = int(line[3])
        except:
            print("No such file exist")        
if __name__ == "__main__":
    data_processor = WeatherDataProcessor()
    n = int(input("Enter the desired option from 1-3 for function execution: "))
    if n==1:
        year_folder_path = input("Enter year and folder path i.e 2005 /home/dev/... : ")
        data_processor.processYearData(year_folder_path)
    elif n==2:
        year_folder_path = input("Enter year and folder path i.e 2005/5 /home/dev/... : ")
        data_processor.processMonthAverage(year_folder_path)
    elif n==3:
        year_folder_path = input("Enter year and folder path i.e 2005/5 /home/dev/... : ")
        data_processor.processMonthPrint(year_folder_path)
