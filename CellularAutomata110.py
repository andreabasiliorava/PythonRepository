CA110 = { "..." : "0", 
          "..0" : ".",
          ".0." : ".",
          "0.." : ".",
          ".00" : "0",          
          "0.0" : ".",
          "00." : ".",
          "000" : "0"
        }
CA110.keys()
CA110.values()

my_state = [".",".",".",".",".",".",".",".",".","."]

def boundary_evolution (state) :
    if state[0] == "0" :
        state[0] = "."
    else :
        state[0] = "0"
    if state[-1] == "0" :
        state[-1] = "."
    else :
        state[-1] = "0"  
    return state
        
print(boundary_evolution(my_state))        
        
#def evolution (state) :
        