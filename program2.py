# #function to simulate the vaccum cleaner agent
# def reflex_vaccum_agent(location,status):
#     if status == "Dirty":
#         return "Suck"
#     elif location == "A":
#         return "Right"
#     elif location == "B":
#         return "Left"
# #test the reflex agent
# #environment location A is dirty,location B is clean initially
# location ="A"
# status ="Dirty"
# #define location
# locations = ["A","B"]
# #simulate agent action
# for _ in range(5):#simulate for 5 iterations
#     #agent's  action
#     action = reflex_vaccum_agent(location,status)
#     print(f"Location : {location},Status : {status},Action : {action}")
#     #update status
#     if action == "Sck":
#         status="clean"
#     elif action == "Clean":
#         location="B"
#     elif action == "left":
#         location="A"
# Function to simulate the vacuum cleaner agent
def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

# Initial environment
location = "A"
status = "Dirty"

# Simulate agent actions for 5 iterations
for _ in range(5):
    action = reflex_vacuum_agent(location, status)
    print(f"Location: {location}, Status: {status}, Action: {action}")
    
    # Update environment based on action
    if action == "Suck":
        status = "Clean"
    elif action == "Right":
        location = "B"
        # assume new location B status (you can change)
        status = "Dirty"  # or "Clean" depending on scenario
    elif action == "Left":
        location = "A"
        status = "Dirty"  # or "Clean" depending on scenario