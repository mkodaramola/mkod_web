import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def getAfterComma(n,packet):
	fc = 0
	j = 0
	i =0
	for c in packet:
		if c == ',':
			j+=1
		if j == n:
			fc = i
			break
		i+=1
	nPacket = packet[(fc+1):]
	
	return (nPacket[0:(nPacket.find(','))])


def HMS_L(t):

	hr = int(t[0:t.find(':')])
	mins = int(t[t.find(':')+1:t.rfind(':')])
	sec = int(t[t.rfind(':')+1:])

	s = (hr*3600) + (mins*60) + sec

	return s

		






# Open the file in read mode
file = open('Flight_1235_C2.csv', 'r')

# Read the contents of the file
content = file.readlines()

# Close the file
file.close()


content.reverse()
content.pop()
content.reverse()


listX = []
listY = []

for line in content:
	listX.append(HMS_L(getAfterComma(1,line)))

for line in content:
	listY.append(getAfterComma(7,line))


print(listX)
print(listY)


# Plot the graph
plt.plot(listX, listY)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph Example')

# Display the graph
plt.show()




print(HMS_L("21:43:12"))
print(HMS_L("21:43:13"))
print(HMS_L("21:44:12"))