with open("given.txt") as lines:
    given_left = []
    given_right = []
    for line in lines:
        given_left.append(int(line.strip().split("   ")[0]))
        given_right.append(int(line.strip().split("   ")[1]))
                     
        def calculate_list_distance(left_list, right_list):
        
            # Sort both lists
            sorted_left = sorted(left_list)
            sorted_right = sorted(right_list)
            
            # # Ensure lists are the same length
            # if len(sorted_left) != len(sorted_right):
            #     raise ValueError("Lists must be of equal length")
            
            # Calculate distances between paired elements
            distances = [abs(left - right) for left, right in zip(sorted_left, sorted_right)]
            
            # Return and print total distance
            total_distance = sum(distances)
            print(f"\nTotal Distance: {total_distance}")
            return total_distance

        
    calculate_list_distance(given_left, given_right)
        
            