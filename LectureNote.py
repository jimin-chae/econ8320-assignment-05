# Course #5 Note
# import re
#import re
# mystring = "I think I'll get a 50."
# re.search() is primary tool in the regular expression 
# search for the pattern in the tool#
# type(re.search(r'[0123456789]', mystring))
# r is raw string without being escaped 
# [charatcer] 
# print("help! I'm being eaten by a boa constrictor!")
# print("help! I'm being eaten by a boa \nconstrictor!") #will give you new line
# print(r"help! I'm being eaten by a boa \nconstrictor!") #won't give you new line, since it's raw string
# r'\n'
# In [4]: re.search(r'[0123456789]',mystring)
# type(re.search(r'[!],mystring)) -> gives you NoneType
# mystring = "I think I will get a 50."
# mystring = "I think I'll get a 10000"

#REPEATING VALUES
# * is Shorthand for 0 or more of character / character class
# + is shorthand for 1 or more of a character / character class
# ? is shorthand for 0 or 1 (like saying "maybe")
# {x,y} is shorthand for.  character that is repeated no less than x times, and no more than y times.
# re.search(r'[0-9]*',mystring)     # 
# re.search(r'[0-9]+',mystring)     # + means one or more reputation
# re.search(r'[0-9]{1,3}',mystring)
# print (re.search)

# Uncertainty
# We can be more stringent in our expectations:
# A percentage with 3 digits can only begin with a 1! Two digit percentages shouldn't lead with a 0, and single digit percentages can be 0 and 9.
# re.search(r'100|[1-9][0-9]|[0-9]', mystring)
# We need a pattern only acceptable for 3 digit number is 100

#re.search(r'100|[1-9][0-9]|[0-9]', mystring) # only valid 3 digit number, if it's too big it won't work e.g.,782 then 78
# We can pick a zero in the middle, we are getting invalid number 
# Boundary Character is needed
# 
# BOUNDARY CHARACTER
# \b represents a word boundary (either at the start or end of a word)
# ^ represents the start of a string
# $ represents the end of a string 

#re.search(r'\b(100|[0-9][1-9][1-9])\b',mystring)

# Not match 101. 
# This word boundary is protecting us from extra numebers floating around us and chopping a chunk out of them.
# We have to be very specific with our regular expression about what is and is not a ift to our pattern.


# Exercise: How can we solve our phone number problem?
#import re
#mystring = "1-425-389-1180"
#re.search(r'\b[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]\b',mystring)
# \d = 0-9
#re.search(r'\d{3}-\d{4}',mystring) #include area code (may or maynot)
#re.search (r'(\d{3}-)?\d{3}-\d{4}',mystring) #? = may vs may not  now we have area code
#re.search (r'(1-)?(\d{3}-)?\d{3}-\d{4}',mystring) # now we have country code
#re.search (r'^(1-)?(\d{3}-)?\d{3}-\d{4}$',mystring) # anything besides phonenumber
#re.search (r'^((1-)?\d{3}-)?\d{3}-\d{4}$',mystring) # put country code inside of the area code, so that invalid phone number won't work for 1-222-2222


#Some Additional Shorthand
# \w - Word Character, denotes any alphanumeric character, or an underscore ([a-zA-Z0-9_])
# \d - denotes any numeric character ([0-9])
# \s - denotes any whitespace character ([ \t\n\r\f\v]): any white space
# \W - the inverse of \w: any none word character
# \D - the inverse of \d: any none digit character
# \S - the inverse of \s: any none white space character

#Exercise: City State Combinations: what if we want to find city, state abbreviation combinations (i.e., Miami, FL) from a text address?
#import re
#mystring = "6708 Pine Street, Omaha, NE 68182"
#mystring = "261 S 800 E\nSalt Lake City, UT 84102" #new line before Salt Lake City
#re.search(r'\w+, [A-Z]{2}', mystring) # our pattern does not match when we have multiple words like space in city name e.g., Omaha is okay but New York City won't work
#re.search(r'\w+( \w+)*, [A-Z]{2}', mystring) 
#try: 
#    result = re.search(r'(\w+(?: \w+)*)(?:, )([A-Z]{2})', mystring).groups() #take it seperately
#except:
#    print("No Match Found")
#    result = re.search(r'(\w+(?: \w+)*)(?:, )([A-Z]{2})', mystring).groups() #take it seperately
#result[1] # would be UT, if there is no ',' then it won't work.
# [.] means anything execpt for line breaks



# Alternate Functionally
# The 're' library offers several functionss:
# 1. re.search: We can search as we have so far
# 2. re.findall: We can search for all matches in a string
# 3. re.finditer: We can generate an iterator to process all matches in a string (related to findall)
# 4. re.split: Use regex to split strings, rather than similar 

