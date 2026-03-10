#function to simulate the vaccum cleaner agent
def reflex_vaccum_agent(location,status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"
#test the reflex agent
#environment location A is dirty,location B is clean
location ="A"
status ="Dirty"
#agent action
action = reflex_vaccum_agent(location,status)
print(f"Location : {location},Status : {status},Action : {action}") 