from time import sleep, time

print('\nYou have 5 tries, we will give you your average reaction time!')

total_time = 0
count = 0

for i in range(5):
    print ('\nTry #',(i+1),'... WAIT...\n')
    sleep(5)
    start = time()
    print ('Quick, the Enter key!')
    input ()
    reaction_time = time() - start
    total_time += reaction_time
    count += 1
    print ('You took {0:.3f} seconds this time!'.format(reaction_time))

average_time = total_time / count

print ('\nYour average reaction time was {0:.3f} seconds!'.format(average_time))
