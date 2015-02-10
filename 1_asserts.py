import congress

# Congressional representatives have:
# - name
# - party
# - state
# - laziness_factor (% of votes missed)

representatives = congress.read_congress_data()

# 1. Make sure that read_congress_data() returns a list object.
assert type(representatives) == list

# 2. Ensure that there are 442 representives.
assert 442 == len(representatives)

# 3. Ensure that each item in the list is of type HouseMember
for rep in representatives:
    assert type(rep) is congress.ElectedOfficial



print("Congratulations, all assertions passed!")
