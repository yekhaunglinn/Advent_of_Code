with open("given.txt") as lines:
    given_left = []
    given_right = []
    for line in lines:
        given_left.append(int(line.strip().split("   ")[0]))
        given_right.append(int(line.strip().split("   ")[1]))

    def calculate_similarity_score(left_list, right_list):
            
            # Count the frequency of each number in the right list
            right_freq = {}
            for num in right_list:
                right_freq[num] = right_freq.get(num, 0) + 1
            
            # Calculate similarity score
            similarity_score = 0
            detailed_scores = []
            
            for num in left_list:
                # Count how many times the number appears in the right list
                freq = right_freq.get(num, 0)
                
                # Calculate the contribution to the similarity score
                score = num * freq
                similarity_score += score
                
                # Store detailed information for explanation
                detailed_scores.append((num, freq, score))
            
            
            print(f"\nTotal Similarity Score: {similarity_score}")
            return similarity_score

    calculate_similarity_score(given_left, given_right)