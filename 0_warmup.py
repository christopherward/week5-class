import congress

# Congressional representatives have:
# - name
# - party
# - state
# - loyalty_factor (% of votes with their party)

representatives = congress.read_congress_data()



#
# Write code to display the correct answers.
#

# 1. What type of object is held inside the 'representatives' variable?
print("Type of object:", type(representatives))

# 2. How many representatives are there?
print("Number of representatives:", len(representatives))

# 3. Display the name of the last representative.
print("Last representative:", representatives[-1].name)

# 4. Which rep is most loyal to their party?
most_loyal = representatives[0]
for rep in representatives:
    if rep.loyalty_factor > most_loyal.loyalty_factor:
        most_loyal = rep
print("Most loyal:", most_loyal.name)
        

# 5. Which rep is a traitor to their party?
least_loyal = representatives[0]
for rep in representatives:
    if rep.loyalty_factor < least_loyal.loyalty_factor:
        least_loyal = rep
print("Least loyal:", least_loyal.name)

# 6. Can you make the following code work?
#    You can modify the congress.py file if you want to.

first_rep = representatives[0]
print("One line: " + first_rep.one_line_display)

#    should display:
#
#    Robert, Aderholt. Republican.

