# Created by Name: Sam Burns

import csv
import datetime
import argparse
from datetime import time

# Definition for the Truck class which uses a list of packages (list of pack ids)
# Also uses a location (distance traveled) and a timestamp (datetime.timedelta)
class Truck:
    # Class constructor
    def __init__(self, packages, location, timestamp):
        self.packages = packages
        self.location = location
        self.timestamp = timestamp

    # Truck location setter
    def set_location(self, new):
        self.location = new

    # Truck packages setter
    def set_packages(self, newlst):
        self.packages = newlst

    # Truck timestamp setter
    def set_timestamp(self, new):
        self.timestamp = new

    # Truck location getter
    def get_location(self):
        return self.location

    # Truck timestamp getter
    def get_timestamp(self):
        return self.timestamp

# Definition of the package class.
# Also uses a timestamp (datetime.timedelta) and a status (string default "At the hub")
class Package:
    # Class constructor
    def __init__(self, timestamp, id, address, city, zip, deadline, mass, status):
        self.timestamp = timestamp
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.mass = mass
        self.deadline = deadline
        self.status = "At the hub"

    # Package Timestamp setter
    def set_timestamp(self, new):
        self.timestamp = new

    # Package Timestamp getter
    def get_timestamp(self):
        return self.timestamp

    # Package ID getter
    def get_id(self):
        return self.id

    # Package delivery address getter
    def get_address(self):
        return self.address

    # Package delivery address setter
    def set_address(self, new):
        self.address = new

    # Package delivery city getter
    def get_city(self):
        return self.city

    # Package delivery zip code getter
    def get_zip(self):
        return self.zip

    # Package delivery zip code setter
    def set_zip(self, new):
        self.zip = new

    # Package mass (in kg) getter
    def get_mass(self):
        return self.mass

    # Package delivery deadline getter
    def get_deadline(self):
        return self.deadline

    # Package delivery status getter
    def get_status(self):
        return self.status

    # Package delivery status setter
    def set_status(self, new):
        self.status = new

    # Print function of package
    def print(self):
        print(f"id:{self.id}, address:{self.address}, timestamp:{self.timestamp}", end=' \n')

# Definition of the Edge class which uses values for a source node, destination node and a weight (aka miles)
# Used to build the Graph object defined below.
class Edge:
    # Class constructor
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight

# Definition of the Address Node class which uses the destination value from the edge class and the edge weight
# Used to build the Graph object defined below.
class AddressNode:
    # Class constructor
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight

# Definition of the GraphObj which builds and dismantles the Graph data structure used in the program
# The class also has a number of functions used in the program including the minimum distance and return edge functions
class GraphObj:
    # Class constructor
    def __init__(self, vect, N):

        self.adj = [None] * N
        self.size = N

        for x in range(N):
            self.adj[x] = []

        for e in vect:
            addnode = AddressNode(e.dest, e.weight)
            self.adj[e.source].append(addnode)

    # Add node function which takes an edge object and creates a new node then appends the node to the graph structure
    def addNode(self, edge):
        addnode = AddressNode(edge.dest, edge.weight)
        self.adj[edge.source].append(addnode)

    # Removes node function that deletes a node from the graph + blanks all edge destination references to that node
    def deleteNode(self, node):
        for source in range(len(self.adj)):
            for neighnode in self.adj[source]:
                if neighnode.val == node:
                    neighnode.val = ''
                    neighnode.weight = ''

        self.adj[node] = []

    # Function to print all information (i.e. nodes and edges) from the referenced graph object
    def printG(graph):
        for source in range(len(graph.adj)):
            for edge in graph.adj[source]:
                print(f"({source} -> {edge.val}, {edge.weight}) ", end=' \n')

    # Function to return the index location of the node with the shortest distance and the distance value (miles.)
    # Sorts a list of flt values (input of 'distances')
    # Returns the lowest flt value and the index location of that value in the original list
    # Critical portion of the nearest neighbor algorithm
    def mindist(self, distances):

        sortdist = sorted(distances)
        sortdist = list(filter(None, sortdist))

        if len(sortdist) != 1:

            out = sortdist.pop(0)

            for i in range(len(distances)):
                var = distances[i]

                if var == out:
                    return i, out;
        else:
            return 0, sortdist[0]

    # Function that takes a node number (int) and returns all edge weight values (aka distances in miles)
    # The function also returns a list of nodes numbers in the same order as the distances list
    def returnEdges(self, num):
        distances = []
        destids = []

        for edge in self.adj[num]:
            if edge.weight != '':
                distances.append(float(edge.weight))
                destids.append(edge.val)

        return distances, destids

# Definition of the Hash map class. This code is from
#
# James, Joe. (2016, Jan 22). Python: Creating a HASHMAP using lists
# [How to implement a hashmap (AKA dictionary, hash table, associative array) in Python using lists / arrays.
# YouTube. URL http://www.youtube.com/watch?v=9HFbhPscPU0

class HashMap:
    # Class constructor
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    # Function to get size of the hashmap
    def get_size(self):
        return self.size

    # Function to calculate the index for the given key
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # Function to a add a new key and value to the referenced hash map
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Function to the get the value of the hashmap associated with the input key
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
            return None

    # Function that removes a key any associated value in the hash map
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop[i]
                return True

    # Function to the print all item of in the referenced hash map
    def print(self):
        print('-----Hash Map -------')
        for item in self.map:
            if item is not None:
                print(str(item))

# Function definition for the lookup package function. Used by the command line interface to return package info
# Input is the package hash map, input value (either a string or integer)
# as well as selection (i.e. 'ID') and then the time in datetime.timedelta()
def lookupPackage(map, input, selection, time):

    if selection == 'ID':
        for x in range(1, map.get_size() + 1):
            package = map.get(str(x))

            if input == int(package.get_id()):
                print(
                    f"  -  ID:{package.get_id()} | Address: {package.get_address()} | City: {package.get_city()} | Zip: {package.get_zip()} | Mass: {package.get_mass()} kg | Deadline: {package.get_deadline()} | Status: {package.get_status()}", end=' ')
                if package.get_status() == 'Delivered':
                    print(f"at {package.get_timestamp()}", end=' \n')
                else:
                    print(f" ", end='\n')

    elif selection == 'Address':
        for x in range(1, map.get_size() + 1):
            package = map.get(str(x))

            if input == package.get_address():
                print(
                    f"  -  ID:{package.get_id()} | Address: {package.get_address()} | City: {package.get_city()} | Zip: {package.get_zip()} | Mass: {package.get_mass()} kg | Deadline: {package.get_deadline()} | Status: {package.get_status()}", end=' ')
                if package.get_status() == 'Delivered':
                    print(f"at {package.get_timestamp()}", end=' \n')
                else:
                    print(f" ", end='\n')

    elif selection == 'City':
        for x in range(1, map.get_size() + 1):
            package = map.get(str(x))

            if input == package.get_city():
                print(
                    f"  -  ID:{package.get_id()} | Address: {package.get_address()} | City: {package.get_city()} | Zip: {package.get_zip()} | Mass: {package.get_mass()} kg | Deadline: {package.get_deadline()} | Status: {package.get_status()}", end=' ')
                if package.get_status() == 'Delivered':
                    print(f"at {package.get_timestamp()}", end=' \n')
                else:
                    print(f" ", end='\n')

    elif selection == 'Zip':
        for x in range(1, map.get_size() + 1):
            package = map.get(str(x))
            if input == int(package.get_zip()):
                print(
                    f"  -  ID:{package.get_id()} | Address: {package.get_address()} | City: {package.get_city()} | Zip: {package.get_zip()} | Mass: {package.get_mass()} kg | Deadline: {package.get_deadline()} | Status: {package.get_status()}", end=' ')
                if package.get_status() == 'Delivered':
                    print(f"at {package.get_timestamp()}", end=' \n')
                else:
                    print(f" ", end='\n')


    elif selection == 'Weight':
        for x in range(1, map.get_size() + 1):
            package = map.get(str(x))

            if input == package.get_mass():
                print(
                    f"  -  ID:{package.get_id()} | Address: {package.get_address()} | City: {package.get_city()} | Zip: {package.get_zip()} | Mass: {package.get_mass()} kg | Deadline: {package.get_deadline()} | Status: {package.get_status()}", end=' ')
                if package.get_status() == 'Delivered':
                    print(f"at {package.get_timestamp()}", end=' \n')
                else:
                    print(f" ", end='\n')


    elif selection == 'Deadline':
        for x in range(1, map.get_size() + 1):
            package = map.get(str(x))

            if input == str(package.get_deadline()):
                print(
                    f"  -  ID:{package.get_id()} | Address: {package.get_address()} | City: {package.get_city()} | Zip: {package.get_zip()} | Mass: {package.get_mass()} kg | Deadline: {package.get_deadline()} | Status: {package.get_status()}", end=' ')
                if package.get_status() == 'Delivered':
                    print(f"at {package.get_timestamp()}", end=' \n')
                else:
                    print(f" ", end='\n')

    elif selection == 'All':
        for x in range(1, map.get_size() + 1):
            package = map.get(str(x))
            print(
                f"  -  ID:{package.get_id()} | Address: {package.get_address()} | City: {package.get_city()} | Zip: {package.get_zip()} | Mass: {package.get_mass()} kg | Deadline: {package.get_deadline()} | Status: {package.get_status()}", end=' ')
            if package.get_status() == 'Delivered':
                print(f"at {package.get_timestamp()}", end=' \n')
            else:
                print(f" ", end='\n')

    else:
        print("FAILED!")

# Function which carries out delivery of the packages in the program.
# Input includes the graph object, a list of nodes, the distance hashmap, the package hashmap, the truck object,
# the package to address hashmap and the time (datetime.timedelta.)
def get_neighbors(graph, nodes, distData, packhash, truck, packmap, time):

    bool = True
    node = 0
    dist_total = truck.get_location()

    for x in range(1, graph.size):

        if len(nodes) == 1 & bool:
            edge = goHome(distData, node)
            graph.addNode(edge)
            bool = False

        edge_tuple = graph.returnEdges(node)
        timestmp = truck.get_timestamp()

        mindist_tuple = graph.mindist(edge_tuple[0])
        destlist = edge_tuple[1]
        dist_val = float(mindist_tuple[1])
        index = mindist_tuple[0]
        newnode = destlist[index]
        dist_total = dist_total + dist_val
        timehr = dist_val / 18
        time_obj = datetime.timedelta(hours=timehr)
        timestmp = timestmp + time_obj

        if timestmp < time:
            truck.set_timestamp(timestmp)
            truck.set_location(dist_total)

            if newnode != 0:
                for x in range(1, packmap.get_size() + 1):
                    ref = packhash.get(x)

                    if ref == newnode:
                        temppackage = packmap.get(str(x))
                        temppackage.set_timestamp(timestmp)
                        temppackage.set_status('Delivered')
            try:
                while True:
                    nodes.remove(newnode)
            except ValueError:
                pass

            if not nodes:
                break

            graph.deleteNode(node)
            node = newnode
        else:
            break

    return timestmp

# Function that inputs the truck object along with the package map ("UPS Package File.cvs" file data)
# along with the hash map and distance list from the "UPS Distance Table.csv" file.
# Returns the list of packages (trucklst), the list of node ids (nodelist) which the truck needs to travel to
# also returns the Graph object with appropiate nodes and edges for delivering the packages as well as
# a hash map object which maps the package id number to the node id number (i.e. address, returns packagehash)
def loadTruck(truck, packageMap, addressMap, distanceData):

    trucklst = truck.packages
    fullnodelist = [0]
    nodelist = []
    edges = []
    packagehash = HashMap(len(trucklst))

    for x in range(len(trucklst)):
        packid = trucklst[x]
        package = packageMap.get(str(packid))
        address = package.get_address()

        for source in range(len(distanceData)):
            mapped = addressMap.get(source)

            if mapped == address:
                fullnodelist.append(source)
                package.set_status("En Route")
                packagehash.add(packid, source)

    #remove duplicate nodes in list
    [nodelist.append(x) for x in fullnodelist if x not in nodelist]

    for y in range(len(nodelist)):
        for z in range(len(nodelist)):
            if z != y:
                edges.append(Edge(nodelist[y], nodelist[z], distanceData[nodelist[y]][nodelist[z]]))

    N = len(edges)

    graph = GraphObj(edges, N)

    return trucklst, nodelist, graph, packagehash

# Function which takes a number (lastnode) corresponding to a node id. The function then returns an edge object
# which uses to the distance data 2D list (address hash map, UPS Distance Table.csv data) to find the distance
# of the inputted last node to the  hub (node 0.)
def goHome(distanceData, lastnode):

    edge = Edge(lastnode, 0, distanceData[lastnode][0])
    return edge

# Function that loads data from the UPS Package File.csv and returns a hash map class object using the package id
# as the key and a new package object as the value. This demonstrates a chained hash map object.
def loadPackages():

    defaulttime = time(0, 0, 0)

    with open('UPS Package File.csv') as packagecsv:
        readCSV = csv.reader(packagecsv, delimiter=',')
        csvData = list(readCSV)

    packageMap = HashMap(40)

    for y in range(8, len(csvData)):
        pack = Package(defaulttime, csvData[y][0], csvData[y][1], csvData[y][2], csvData[y][4], csvData[y][5], csvData[y][6],"En Route")
        packageMap.add(csvData[y][0], pack)

    return packageMap

# Function that loads data from the UPS Distance Table.csv
# Returns "distanceData" 2D list of distances with first index value equal
# to the key of the address hash map also returned by the function
# for example the hub is node 0 and the edge distances from the hub are at index 0 of the distanceData list.
# The function also edits an address string with "Sta" into "Station" to match package addresses.
def loadDistance():
    with open('UPS Distance Table.csv') as csvfile:

        addressMap = HashMap(26)

        readCSV = csv.reader(csvfile, delimiter=',')
        csvData = list(readCSV)

        for y in range(2, 29):
            address = csvData[7][y]
            #strip lettering here
            if y == 2:
                temp = address.partition("\n")[2]
                str = temp.partition("\n")[0]
                str = str.rstrip(", ")
            else:
                temp = address.partition("\n")[2]
                str = temp.lstrip()

            # corrects Sta into Station for proper searching
            if y == 18:
                str = str[:25] + "tion" + str[25:]

            addressMap.add((y - 2), str)

        distanceData = []
        iterate = 0

        for x in range(2, 29):
            nest = []

            for y in range(8, len(csvData)):
                dist = csvData[y][x]
                nest.append(dist)

            distanceData.append(nest)


        for z in range(1, len(distanceData)):
            iterate += 1

            for t in range(0, iterate):
                temp = distanceData[t][z]
                distanceData[z][t] = temp

    return distanceData, addressMap

# Call of the load distance function which returns the Distance Table data.
tuple = loadDistance()
distanceData = tuple[0]
addressMap = tuple[1]

# Here the command line interface arguements are defined. Allows users to look up packages by id, address
# city, zip or deadline. The user can also input a time and see the status of each package and the trucks
# as long as the time is inputted as military time (i.e. 1300 for 1pm)
parser = argparse.ArgumentParser(description="Enter a time after 08:00:00 (in military time, i.e., 0900) to check package status or 'exit()' to exit. Enclose all inputs in double quote")
parser.add_argument("--time", type=str, nargs=1, metavar="Packages at time lookup", help="input time in military time")
parser.add_argument("--package_id", type=str, nargs=1, metavar="Package ID lookup", help="input package ID #")
parser.add_argument("--package_address", type=str, nargs=1, metavar="Package address lookup", help="input package address")
parser.add_argument("--package_city", type=str, nargs=1, metavar="Package city lookup", help="input package city")
parser.add_argument("--package_zip", type=int, nargs=1, metavar="Package zip code lookup", help="input zip code")
parser.add_argument("--package_deadline", type=str, nargs=1, metavar="Package deadline lookup", help="input package deadline")


# Prints menu to the command line interface when the program is run.
print("Enter a time after 08:00 (in military time, i.e., 0900) to check package status or 'exit()' to exit. Enclose all inputs in double quotes.")
print("'python3 main.py --time [value]' and the number in '0900' format for value")
print("'python3 main.py --package_id [value]' and the number (i.e. '1') format for value")
print("'python3 main.py --package_address [value]' and the address (i.e.'195 W Oakland Ave') format for value")
print("'python3 main.py --package_city [value]' and the city name (i.e. 'Salt Lake City') format for value")
print("'python3 main.py --package_zip [value]' and the zip code (i.e. '84115') format for value")
print("'python3 main.py --package_deadline [value]' and the deadline (i.e. '10:30 AM') format for value\n")

# Parser for the command line interface arguments
args = parser.parse_args()

print("RESULT")

# Declaration of the hour variable datetime.timedelta object
hour = datetime.timedelta(hours=0, minutes=0)

# Evaluates the time argument and parses the '0900' input into 09 hours and 00 minutes. Sets the hour variable
if args.time:
    tmp = args.time[0]
    hr = int(tmp[:2])
    min = int(tmp[2:])
    hour = datetime.timedelta(hours=hr, minutes=min)

# Variable which sets the time (datetime obj) when the address for package #9 is updated.
switch = datetime.timedelta(hours=10, minutes=20)

# Variable which sets the time (datetime obj) when trucks are allowed to leave the hub.
start = datetime.timedelta(hours=8, minutes=0)

# Manual load of Truck 1 which leaves the hub at 8:00 AM
truck1 = Truck([1, 13, 14, 15, 16, 19, 20, 40], 0, datetime.timedelta(hours=8, minutes=0))

# Manual load of Truck 2 which leaves the hub at 9:05 AM
truck2 = Truck([6, 25, 29, 30, 31, 34, 37], 0, datetime.timedelta(hours=9, minutes=5))

# Evaluates the hour variable with start time (i.e. trucks won't load/drive until 8 AM)
iszero = hour <= start

# Evalutes if the inputted time variable (hour) is greater than the time when package 9 address is updated.
result = hour >= switch

# Runs once inputted time is past 8 AM
if not iszero:
    # Package data is loaded
    packages = loadPackages()

    # updates the address of package 9 if time is set to greater than or equal to 10:20 (military time)
    if result:
        package_update = packages.get(str(9))
        package_update.set_address('410 S State St')
        package_update.set_zip(84111)

    # Truck 1 is loaded and the corresponding node list, graph object and package hash map are returned.
    returner = loadTruck(truck1, packages, addressMap, distanceData)
    nodes = returner[1]
    graphobj = returner[2]
    packagehash = returner[3]

    # The greedy nearest neighbor algorithim is run on the graphobj for truck 1.
    # Returns the datetime.timedelta of the truck after completing its route.
    ts_1 = get_neighbors(graphobj, nodes, distanceData, packagehash, truck1, packages, hour)

    # Truck 2 is loaded and the corresponding node list, graph object and package hash map are returned.
    returner = loadTruck(truck2, packages, addressMap, distanceData)
    nodes = returner[1]
    graphobj = returner[2]
    packagehash = returner[3]

    # The greedy nearest neighbor algorithim is run on the graphobj for truck 2.
    # Returns the datetime.timedelta of the truck after completing its route.
    ts_2 = get_neighbors(graphobj, nodes, distanceData, packagehash, truck2, packages, hour)

    # Evaluates if inputted time is greater than the returned time of truck 1 and 2 after their first route.
    result2 = hour >= ts_2
    result3 = hour >= ts_1

    # Truck 2 is loaded manually with half of the remaining packages (list of package Id's)
    truck2.set_packages([2,3,7,8,9,10,18,27,33,35,36,38,39])
    # Truck 1 is loaded manually with the remaining packages.
    truck1.set_packages([4,5,11,12,17,21,22,23,24,26,28,32])

    # Runs if inputted time >= previous return time for truck 2
    if result2:
        # Truck 2 is loaded and the corresponding node list, graph object and package hash map are returned.
        returner = loadTruck(truck2, packages, addressMap, distanceData)
        nodes = returner[1]
        graphobj = returner[2]
        packagehash = returner[3]
        # The greedy nearest neighbor algorithim is run on the graphobj for truck 2.
        get_neighbors(graphobj, nodes, distanceData, packagehash, truck2, packages, hour)

    # Runs if inputted time >= previous return time for truck 1
    if result3:
        # Truck 1 is loaded and the corresponding node list, graph object and package hash map are returned.
        returner = loadTruck(truck1, packages, addressMap, distanceData)
        nodes = returner[1]
        graphobj = returner[2]
        packagehash = returner[3]
        # The greedy nearest neighbor algorithim is run on the graphobj for truck 1.
        get_neighbors(graphobj, nodes, distanceData, packagehash, truck1, packages, hour)

    print("Current time:", hour)

    # Print statement for all the package data. Used to show command line interface user all package data
    # after inputting a specific time
    lookupPackage(packages, ' ', 'All', hour)

    # Prints the total miles traveled by all three trucks. Truck 3 was not used so miles traveled = 0.
    print(f"Total miles traveled by Truck 1: {truck1.get_location()}")
    print(f"Truck 1 Timestamp: {truck1.get_timestamp()}")
    print(f"Total miles traveled by Truck 2: {truck2.get_location()}")
    print(f"Truck 2 Timestamp: {truck2.get_timestamp()}")
    print("Total miles traveled by Truck 3: 0 (not used)")
else:
    # Loads the package data even if the --time command line argument is not used
    packages = loadPackages()

    # Allows the user to lookup package data without running the algorithm. each argument will print information based
    # on the input (i.e. 'ID')
    if args.package_id:
        print("Current time:", hour)
        lookupPackage(packages, int(args.package_id[0]), 'ID', hour)
    elif args.package_address:
        print("Current time:", hour)
        lookupPackage(packages, args.package_address[0], 'Address', hour)
    elif args.package_city:
        print("Current time:", hour)
        lookupPackage(packages, args.package_city[0], 'City', hour)
    elif args.package_zip:
        print("Current time:", hour)
        lookupPackage(packages, int(args.package_zip[0]), 'Zip', hour)
    elif args.package_deadline:
        print("Current time:", hour)
        lookupPackage(packages, args.package_deadline[0], 'Deadline', hour)
    else:
        print("Current time:", hour)
        print("Trucks haven't left the hub yet")

