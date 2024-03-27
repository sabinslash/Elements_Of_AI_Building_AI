def permutations(route, ports, D, co2):
    # Base case: If the length of the route is equal to the length of ports, calculate and print emissions
    if len(route) == len(ports):
        distance = sum(D[route[i]][route[i+1]] for i in range(len(route)-1))
        emissions = distance * co2
        print(' '.join([ports[i] for i in route]) + " %.1f kg" % emissions)
    else:
        # Iterate through each port index in ports
        for i in range(len(ports)):
            # If the current port index is not already in the route
            if i not in route:
                # Recursively call permutations function with the updated route
                permutations(route + [i], ports, D, co2)

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # Distances between ports in kilometers
    D = [
            [0, 8943, 8019, 3652, 10545],
            [8943, 0, 2619, 6317, 2078],
            [8019, 2619, 0, 5836, 4939],
            [3652, 6317, 5836, 0, 7825],
            [10545, 2078, 4939, 7825, 0]
        ]

    # CO2 emissions per kilometer (g per km per metric ton)
    co2 = 0.020

    # Start the recursion with 0 ("PAN") as the first stop
    permutations([0], portnames, D, co2)

main()

