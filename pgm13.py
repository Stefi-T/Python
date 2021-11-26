import operator
d={'february':28,'january':31,'april':30,'march':31,'june':30}
sd=sorted(d.items())
sdr=sorted(d.items(),reverse=True)
print("Ascending order:")
print(sd)
print("Descending oreder:")
print(sdr)
