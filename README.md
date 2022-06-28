# PackageDeliveryApp
Python application that uses addresses and distances to calculate a solution to the travelling salesman problem for a package delivery company.

Run Instructions:

To run the application command line interface first set the current directory to the application folder then run the 
main.py script “python3 main.py”.
	To run commands run the main.py script with the command and lookup value added on. 
NOTE: Input values with double quotation marks “[value]”
Example: [python3 main.py –time “1130”] 
•	The above command will run the program with time set to 11:30 AM
Example: [python3 main.py –package_id “5”]
•	Above example will lookup package information for the package with id # 5. 
Example: [python3 main.py –package_zip “84115”]
•	Command will lookup package information for packages to be delivered to zip code 84115.

The command line interface will first display: 
“Enter a time after 08:00 (in military time, i.e., 0900) to check package status or 'exit()' to exit. Enclose all inputs in double quotes.
'python3 main.py --time [value]' and the number in '0900' format for value
'python3 main.py --package_id [value]' and the number (i.e. '1') format for value
'python3 main.py --package_address [value]' and the address (i.e.'195 W Oakland Ave') format for value
'python3 main.py --package_city [value]' and the city name (i.e. 'Salt Lake City') format for value
'python3 main.py --package_zip [value]' and the zip code (i.e. '84115') format for value
'python3 main.py --package_deadline [value]' and the deadline (i.e. '10:30 AM') format for value “

If the user inputs the command with the proper command (in double quotes) the user can interact with the program. 

Algorithm Information:

The Algorithm used in the program would be described as a Nearest Neighbor algorithm. The program works by building a weighted graph structure with each “edge weight” 
being the miles between nodes (aka. Addresses.) The algorithm then starts at the WGU hub node and then selects the shortest weighted edge connecting the current node and 
an unvisited node (“greedy”.) The unvisited vertex then becomes the current node and the previously visited node is removed from the graph object. Once all nodes have 
been visited the program adds an edge back to node zero (WGU Hub) and the program completes.  

The algorithm has a worst case run time complexity of O(n2 log n). This is due to the main function of the program being the Nearest Neighbor function which has a for-
loop through the graph structure of size (n) and each time calls the minimum distance function which calls the python sort()which has a worst case run time of O(n log n) 
thus the worst case total run time of  the algorithm is O(n2 log n). The next longest runtime would be the same looped call of the minimum distance function that has 
another nested loop which evaluates the distance list of size (n) for a total runtime of O(n2).

