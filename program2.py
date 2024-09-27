def decode_message( s: str, p: str) -> bool:

# write your code here
  # program2.py

def decode_message(s, p):
    # Check if the lengths match unless there is a wildcard that can match any length
    if len(s) != len(p):
        return False

    # Iterate over the characters in both the string and the pattern
    for i in range(len(s)):
        if p[i] == '*':
            # If there is a '*', it can match any character, so continue
            continue
        elif p[i] == '?':
            # '?' can match any single character, so continue
            continue
        elif s[i] != p[i]:
            # If characters don't match, return False
            return False
    
    # If all characters match the pattern, return True
    return True

        return False
