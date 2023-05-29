def calculate_overall_score(scores):
    weights = {0: 0.33, 1: 0.3, 2: 0.27, 3: 0.23, 4: 0.2, 5: 0.17, 6: 0.13, 7: 0.1, 8: 0.07, 9: 0.03}
    count = 0  # Initialize count of scored soft skills

    for score in scores:
        if score.isdigit():
            count += 1

    if count in weights:
        return weights[count] * 100  # Multiply the weight by 100 to get the percentage
    else:
        return 0  # Auto fail if none of the soft skills are scored

soft_skill_scores = ['1', '2a', '8', '9', '10', '11', '12', '13', '15', '17', '20', '21', '22', '23', '24', '25', '26', '28', '29', '31']
overall_score = calculate_overall_score(soft_skill_scores)
print(f"Overall Score: {overall_score}%")
