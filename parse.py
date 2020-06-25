f = open("gps_logger.txt")

lines = f.readlines()
for num, line in enumerate(lines):
    filtered = line.replace("[","").replace("]","").replace("\"","").replace("\r","").replace("\n","")
    listify = filtered.split(",")
    # print(str(num), filtered.split(","))

    filename = "porto_taxi/trip_" + str(num) + ".csv"
    f = open(filename, "a")

    for i in range(len(listify)):
        # single_trip = listify[i] + "," +listify[i+1]
        # f.write(single_trip)
        if (i % 2) == 0:
            # nxt = i + 1
            try:
                single_trip = listify[i].strip(" ") + "," +listify[i+1].strip(" ") + "\n"
                f.write(single_trip)
                # print(listify[i], listify[i+1])
            except:
                print("pass")

    f.close()

f.close
