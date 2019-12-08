import csv

if __name__ == "__main__":

    files = ['data/2018-2019 data pt 1_Oct 01 2018 to Jan 31 2019.csv','data/2018-2019 data pt 2_ Feb 01 2019 to May 31 2019.csv' ]

    result = {}

    for file in files:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            f = open("missing_data.txt", "a+")
            for row in csv_reader:
                date = row[7].split()
                #print(date[0])

                user_id = row[0]
                temp = row[6]
                outdoor_temp = row[8]
                violations = row[9]

                if outdoor_temp != "" and outdoor_temp != "outdoor_temp":
                    if date != "created at":

                        if int(outdoor_temp) < 40:

                            if user_id is not None and user_id != 'user_id':
                                if user_id+"_"+date[0] not in result and temp is not None:
                                    result[user_id+"_"+date[0] ] = [int(temp)]
                                elif temp is not None:
                                    result[user_id+"_"+date[0] ].append(int(temp))

    total_flux_vio = []
    total_flux = []
    for key in result.keys():
        result[key].reverse()
        minim = result[key][0]

        for temp in result[key]:
            if temp < minim - 10 and min(result[key]) < 62:
                print("For user {}, there was a violation and flux in tempeature. The min temp recorded was {} and the max temp recorded was {}. The outside temp was {}".format(key, min(result[key]),max(result[key]), outdoor_temp ) )
                userId = (key.split("_"))[0]
                if userId not in total_flux_vio:
                    total_flux_vio.append(userId)


                minim = temp
            if temp < minim - 10:

                print("For user {}, there was a flux in temperature and no violation. The min temp recorded was {} and the max temp recorded was {}. The outside temp was {}".format(key, min(result[key]),max(result[key]), outdoor_temp ) )
                minim = temp
                userId = (key.split("_"))[0]
                if userId not in total_flux:
                    total_flux.append(userId)
    print(len(total_flux_vio)) #violations
    print(len(total_flux))