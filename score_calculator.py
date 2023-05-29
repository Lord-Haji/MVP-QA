
def calculate_overall_score(scores):
    weights = {0: 0.33, 1: 0.3, 2: 0.27, 3: 0.23, 4: 0.2, 5: 0.17, 6: 0.01, 7: 0.1, 8: 0.07, 9: 0.03}
    count = scores.count(1)  # Count the number of soft skills scored

    if count in weights:
        return weights[count] * 100  # Multiply the weight by 100 to get the percentage
    else:
        return 0  # Auto fail if none of the soft skills are scored