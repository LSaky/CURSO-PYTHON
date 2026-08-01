#AND
and1 = 5 == 5 & 5 == 5 #Devuelve TRUE
and2 = 5 < 2 & 5 == 5 #Devuelve FALSE
and3 = 5 == 5 & 5 < 2 #Devuelve FALSE
and4 = 5 < 2 & 5 < 2 #Devuelve FALSE

#OR
or1 = (5 == 5) | (5 == 5) #Devuelve TRUE
or2 = (5 < 2) | (5 == 5) #Devuelve TRUE
or3 = (5 == 5) | (5 < 2) #Devuelve TRUE
or4 = (5 < 2) | (5 < 2) #Devuelve FALSE


#NOT
#not1 = NOT 5 == 5 #Devuelve FALSE 
#not2 = NOT 5 < 2 #Devuelve TRUE

print(or1)