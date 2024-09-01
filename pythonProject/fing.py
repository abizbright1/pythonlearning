greet = 'what are you saying'
nn = greet.replace('what', 'what the fuck')
print(nn)
sppos = nn.find('the')

ww = nn.find('saying', sppos)
final = nn[sppos+1: ww]
print(final)
sm = open(cvs)