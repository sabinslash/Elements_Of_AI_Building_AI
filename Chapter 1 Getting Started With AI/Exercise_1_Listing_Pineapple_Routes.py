def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Check if the route is valid (contains all ports exactly once)
                    if set(route) == set(range(5)):
                        # Print the route if it's valid
                        print(' '.join([portnames[i] for i in route]))

main()
