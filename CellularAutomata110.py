#%%
#definition of Maps for Cellular Automata 110
CA110 = { "..." : "0", 
          "..0" : ".",
          ".0." : ".",
          "0.." : ".",
          ".00" : "0",          
          "0.0" : ".",
          "00." : ".",
          "000" : "0"
        }
#CA110.keys()
#CA110.values()
#CA110["..."]
"""
a = "fr"
b= " tr yt"
c= a+b
print(c)
"""

my_state = ["0",".",".","0","0","0",".",".","0","."]
"""
my_state[1]= CA110[my_state[0]+my_state[1]+my_state[2]]
print(my_state)
"""
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
        
#print(boundary_evolution(my_state))   
"""
i=1    
CA110[my_state[i-1]+my_state[i]+my_state[i+1]]   
"""        
#print(len(my_state))

def evolve (state) :
    dummy_state = state
    i = 1
    while i < (len(state)-1):
        dummy_state[i]=CA110[state[i-1]+state[i]+state[i+1]]
        i+=1
    boundary_evolution(dummy_state)
    state = dummy_state

def evolution_printer(state,n):
    i=1
    while i <= n:
        print(state)
        evolve(state)
        i+=1
        
evolution_printer(my_state,100)
#%%
        
   
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        