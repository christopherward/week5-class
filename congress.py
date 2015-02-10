import json

class ElectedOfficial:
  #class-level attribute
  parties = ["D", "R", "I"]

  def __init__(self, data = None): # assign initial value of None to data -- only assigns None if data is not passed
    self.name = "{0}, {1}".format(data["last_name"], data["first_name"])
    self.party = data["party"]
    self.state = data["state"]
    self.loyalty_factor = float(data["votes_with_party_pct"])

  #class-level method
  def select_all_from_state(desired_state):

  #def one_line_display(self):
    #return "{0} is a member of the {1} party.".format(self.name, self.party)



  #def read_congress_data():
    with open("congress.json") as f:
      data = json.load(f)

    rep_data = data["results"][0]["members"]
    member_list = []

    for person in rep_data:
      if person["state"] == desired_state:
        person = ElectedOfficial()
        person.name = "{0}, {1}".format(person["last_name"], person["first_name"])
        person.party = person["party"]
        person.state = person["state"]
        person.loyalty_factor = float(person["votes_with_party_pct"])
        member_list.append(person)

    return member_list


