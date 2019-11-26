import csv

if __name__ == "__main__":

    files = ['data/2018-2019 data pt 1_Oct 01 2018 to Jan 31 2019.csv','data/2018-2019 data pt 2_ Feb 01 2019 to May 31 2019.csv' ]

    result = {}

    for file in files:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            f = open("missing_data.txt", "a+")
            for row in csv_reader:
                user_id = row[0]
                temp = row[6]
                outdoor_temp = row[8]
                violations = row[9]

                if outdoor_temp != "" and outdoor_temp != "outdoor_temp":

                    if int(outdoor_temp) < 40:

                        if user_id is not None and user_id != 'user_id':
                            if user_id not in result and temp is not None:
                                result[user_id] = [int(temp)]
                            elif temp is not None:
                                result[user_id].append(int(temp))


    for key in result.keys():

        if max(result[key]) - min(result[key]) > 10:
            print("For user {}, the min temp recorded was {} and the max temp recorded was {}. The outside temp was {}".format(key, min(result[key]),max(result[key]), outdoor_temp ) )
