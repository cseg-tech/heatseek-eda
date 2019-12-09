import csv

global total_ids_num

if __name__ == "__main__":
    total_ids_num = 0
    files = ['data/2018-2019 data pt 1_Oct 01 2018 to Jan 31 2019.csv','data/2018-2019 data pt 2_ Feb 01 2019 to May 31 2019.csv' ]
    lines_seen = set()
    total_ids = set()

    file = files[0] #need to change files[1] or files[0]
    for fileee in files:
        with open(fileee) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            f = open("missing_data.txt", "a+")
            f.write("User IDs of people with incomplete data from:\n" + fileee)

            for row in csv_reader:
                if row[0] not in total_ids:
                    total_ids.add(row[0])

                if row[6] in (None, ""):

                    if row[0] not in lines_seen:
                        f.write(row[0])
                        f.write ("\n")
                        lines_seen.add(row[0])



        #lines_seen.clear()
        total_ids_num += len(total_ids)
    f = open("missing_data.txt", "r+")
    print(str(total_ids_num) + " sensors, " + str(len(lines_seen)) + " sensor failures", file = f )
    try:
        fails = len(lines_seen)/  total_ids_num
    except:
        fails = total_ids_num
    print( str(fails) + "% of sensors failed\n", file = f)



#write into new csv
