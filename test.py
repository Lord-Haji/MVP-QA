# import re

# string = '''1. True - The agent mentioned his name as Varun Haukannahal.
# 2. False - The agent did not inquire about RACT Number (Tasmania only).

# Section 2: Compliance
# 3. True - The agent presented the product accordingly.
# 4. True - The agent tailored his approach when the customer clearly indicated that he is after information only and offered the customer requested with the option of follow up in a few days to help with comparisons and selecting the right electricity/gas plan.
# 5. True - The agent clearly explained that the Welcome Pack is a contract binding document.
# 6. True - The agent advised and the customer clearly understood about the cooling off period.
# 7. True - The agent gave the customer a conscionable decision.
# 8. 
# 8.a. False - The customer did not sound aloof.
# 8.b. False - The customer did not sound confused.
# 8.c. False - There was no indication of hearing issues.
# 8.d. False - The customer did not repeat themselves.
# 8.e. False - The customer did not question continuously what the call is all about.
# 9. True - The agent did not use potential misleading or deceptive statements.

# Section 3: Authorized contact
# 10. False - The customer did not indicate/state they are not authorized to conduct the transfer.

# Section 3: Obtaining and Presenting Skills
# 11. True - The agent confirmed Life Support.
# 12. True - The agent confirmed the supply address.
# 13. True - The agent confirmed Concession.
# 14. True - The agent offered to read out the rates.
# 15. True - The agent offered to do Bill Comparison.
# 16. True - The agent provided an estimation for low, medium, and high usage in VIC.
# 17. True - The agent answered customer questions correctly.

# Section 4: Soft Skills
# 18. True - The agent avoided long silences during the call.
# 19. True - The agent ensured they did not interrupt the customer while they spoke.
# 20. True - The agent displayed a professional manner throughout the call.
# 21. True - The agent proactively added value throughout the call.
# 22. True - The agent sounded clear and confident throughout the call.
# 23. True - The agent refrained from using jargon during the call.
# 24. True - The agent sounded friendly, polite, and welcoming.
# 25. True - The agent used effective questioning skills.
# 26. True - The agent demonstrated active listening'''

# true_lines = [line for line in string.splitlines() if 'True' in line]
# true_numbers = [re.search(r'(\d+)\.', line).group(1) for line in true_lines]
# true_numbers = [int(num) for num in true_numbers]
# print(true_numbers)
from scores import scores_dict


converted_string = "inboundmoveinsale"


true_numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# print(len(true_numbers))

report = ""

# print(len(scores_dict.get("inboundretention")))

# print(sum(scores_dict.get("inboundretention")))

total_score = sum(scores_dict.get(converted_string, [0])[param - 1] for param in true_numbers)


report += "\n" + str(total_score) + "\t"

if total_score > 80:
    report += "Pass"
        
else:
    report += "Fail"

print(report)


