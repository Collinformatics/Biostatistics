from functions import compairSets, describeSet


data = [12.0,9.5,13.5,7.2,10.5,6.3,12.5]
tag = 'Initial Set'
dataStats = describeSet(data, tag)

data2 = [12.0,9.5,13.5,7.2,10.5,1.5,12.5]
tag2 = 'Dataset 2'
data2Stats = describeSet(data2, tag2)
compairSets(data1=dataStats, tag1=tag, data2=data2Stats, tag2=tag2)

data3 = [12.0,9.5,13.5,7.2,10.5,6.3,12.5,14.9,7.9,5.2,13.1,10.7,6.5]
tag3 = 'Dataset 3'
data3Stats = describeSet(data3, tag3)
compairSets(data1=dataStats, tag1=tag, data2=data3Stats, tag2=tag3)
