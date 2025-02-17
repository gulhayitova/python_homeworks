universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(unilist):
    num = list()
    tui = list()
    for i in unilist:
        num.append(i[1])
        tui.append(i[2])
    return num, tui
def mean(stat):
    return (sum(stat))/len(stat)
def median(stat):
    stat.sort()
    if len(stat)%2 == 1:
        return stat[len(stat)//2]
    else: 
        return (stat[len(stat)//2]+stat[len(stat)//2+1])//2
print(f"Total students: {sum(enrollment_stats(universities)[0])}")
print(f"Total tuition: ${sum(enrollment_stats(universities)[1])}\n")
print(f"Student mean: {mean(enrollment_stats(universities)[0]):.2f}")  
print(f"Student median: {median(enrollment_stats(universities)[0])}\n")
print(f"Tuition mean: ${mean(enrollment_stats(universities)[1]):.2f}")
print(f"Tuition median: ${median(enrollment_stats(universities)[1])}")