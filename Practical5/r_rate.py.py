r=1.2
n=84


for i in range(1,6): #Do five cycles
    n=n+n*r #Count the total number of people infected at the end of each round
print("number of infected individuals after 5 rounds of infectionn:",n)
