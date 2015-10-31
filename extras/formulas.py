force = 100
distance = 1
time = 10

#Imperial measurements only
work = force * distance
power = force * distance / time # in ft lbs/sec
watts = power * 1.355817948 # convert from ft lbs/sec to watts
print(power)
print(watts)

#Metric measurments only
force = weight
distance = gravity x height of pull
gravity = 9.8 # m/s2
work = force * distance
power = force * distance / time


