# Altitude of a satellite
# G= 6.67*10e-7
# M=6*10e24
print("ANSWER TO PART A:")


def altitude(T):
    r = (256686) * (T**(2 / 3))
    return r


T = input("Enter the Time period::")
T = float(T)
r = altitude(T)

print("The altitude is ::%f m" % (r))

print("ANSWER TO PART B:")

r = altitude(86400.0)
print("The altitude for geosynchronous orbit is ::%f m" % (r))
r = altitude(5400.0)
print("The altitude for T=90 min is ::%f m" % (r))
r = altitude(2700.0)
print("The altitude is T=45 min is ::%f m" % (r))

print("ANSWER TO PART C:")
diff = r = altitude(86400.0) - altitude(86148.0)
print("The difference between the altitude is :%f m" % (diff))
