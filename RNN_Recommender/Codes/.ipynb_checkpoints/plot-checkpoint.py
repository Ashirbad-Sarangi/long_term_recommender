import pandas as analytics
import matplotlib.pyplot as graph

filenames = ['sl-cold','rl-cold','pop','epsilon-greedy']
dfs = []

for file in filenames :
    dfs.append(analytics.read_csv(file+".csv"))

df_sl = dfs[0]
df_rl = dfs[1]
df_pp = dfs[2]
df_eg = dfs[3]

figure = graph.figure(figsize = (20,10))

for i in range(len(dfs)):
    df = dfs[i]
    graph.plot(df['10'],label = filenames[i])

graph.title('Hit@10')
graph.ylabel('Hit Rate')
graph.xlabel('No. of samples')
graph.legend()
graph.show()

graph.savefig('hit@10.png', dpi = 500)