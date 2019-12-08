# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

# Example 1:

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

def reorderLogFiles(logs):
    result = []
    letter_logs = []
    digit_logs = []

    for log in logs:
        s_log = log.split(' ')
        if s_log[1].isalpha():
            letter_logs.append(log)
        else:
            digit_logs.append(log)
    
    # now I need a custom sort function applied to letter_logs
    def sortFn(s):
        s_split = s.split(' ')
        return s_split[1:]

    letter_logs.sort(key = sortFn)
    
    result = letter_logs + digit_logs

    return result



result = reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print('hi')