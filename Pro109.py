import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import pandas as pd
import statistics
import random

df=pd.read_csv('student_performance.csv')
result=df['writing score'].tolist()

for i in range(0,1000):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    sum=d1+d2
    result.append(sum)

mean=statistics.mean(result)
median=statistics.median(result)
mode=statistics.mode(result)
stdev=statistics.stdev(result)
print(stdev)
print(mean,median,mode)

first_stdev_start=mean-stdev
first_stdev_end=mean+stdev
first_data=[result for result in result if result>first_stdev_start and result<first_stdev_end]
print(len(first_data)*100.0/len(result))

second_stdev_start=mean-2*stdev
second_stdev_end=mean+2*stdev
second_data=[result for result in result if result>second_stdev_start and result<second_stdev_end]
print(len(second_data)*100.0/len(result))

third_stdev_start=mean-3*stdev
third_stdev_end=mean+3*stdev
third_data=[result for result in result if result>third_stdev_start and result<third_stdev_end]
print(len(third_data)*100.0/len(result))

graph=pff.create_distplot([result],['Result'],show_hist=False)
graph.add_trace(pgo.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name="Mean"))
graph.add_trace(pgo.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode='lines',name="First Standard Deviation Start"))
graph.add_trace(pgo.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode='lines',name="First Standard Deviation End"))
graph.add_trace(pgo.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode='lines',name="Second Standard Deviation Start"))
graph.add_trace(pgo.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode='lines',name="Second Standard Deviation End"))
graph.add_trace(pgo.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode='lines',name="Third Standard Deviation Start"))
graph.add_trace(pgo.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode='lines',name="Third Standard Deviation End"))
graph.show()