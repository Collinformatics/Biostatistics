from functions import compairSets, describeSet


data = [12.0,9.5,13.5,7.2,10.5,6.3,12.5]
tag = 'Initial Set'
dataStats = describeSet(data, tag)

data2 = [12.0,9.5,13.5,7.2,10.5,1.5,12.5]
tag2 = 'Dataset 2'
data2Stats = describeSet(data2, tag2)
compairSets(data1=dataStats, tag1=tag, data2=data2Stats, tag2=tag2)
