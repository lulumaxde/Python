
def days_needed(kellyDaily, samDaily, difference):
    if samDaily >= kellyDaily and difference >= 0:
      return -1 
    kellyTotal = kellyDaily
    samTotal = difference + samDaily
    count = 1
    while kellyTotal <= samTotal:
        kellyTotal += kellyDaily
        samTotal += samDaily
        count += 1
    return count 

def main():

    samDaily = 3
    kellyDaily = 5
    difference = 1
    print(days_needed(kellyDaily,samDaily,difference))

main()