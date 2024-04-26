import pandas as analytics
import seaborn as sns
import matplotlib.pyplot as graph

filenames = ['sl-cold','rl-cold','pop','epsilon-greedy']
dfs = []

for file in filenames :
    dfs.append(analytics.read_csv(file+".csv"))

df_sl = dfs[0]
df_rl = dfs[1]
df_pp = dfs[2]
df_eg = dfs[3]


def plot_for(N):
    figure = graph.figure(figsize = (15,7))
    for i in range(len(dfs)):
        df = dfs[i]
        graph.plot(df[N],label = filenames[i])


    sns.set_style("whitegrid")
    sns.set_palette("colorblind")

    font = "MathJax_Main"

    graph.title('Hit@'+str(N),fontsize=16, fontweight='bold', fontname=font)
    graph.ylabel('Hit Rate',fontsize=14, fontname=font)
    graph.xlabel('No. of samples',fontsize=14, fontname=font)
    graph.legend(loc='upper right')

    fig1 = graph.gcf()
    graph.show()
    graph.draw()

    fig1.savefig('hit@'+str(N)+'.svg', dpi = 500)


N_values = ['10','10','15','20']

for N in N_values :
    plot_for(N)

filenames = ['rl','sl','eg','pp']
ts = ['10','15','20']

dfs = []
data = {}
for t in ts :
    for file in filenames:
        N = t
        df = analytics.read_csv(file+"_values.csv")
        dfs.append(df)
        data.update({file:df[t]})
        
    
    df_values = analytics.DataFrame(data)
    sns.set_style("whitegrid")
    sns.set_palette("colorblind")
    
    figure = graph.figure(figsize = (15,7))
    graph.plot(df_values['rl'],label = 'rl')
    graph.plot(df_values['sl'],label = 'sl')
    graph.plot(df_values['eg'],label = 'eg')
    graph.plot(df_values['pp'],label = 'pp')
    
    
    font = "MathJax_Main"
    
    
    graph.title('Avg Hit@'+str(N),fontsize=16, fontweight='bold', fontname=font)
    graph.ylabel('Hit Rate',fontsize=14, fontname=font)
    graph.xlabel('Progress',fontsize=14, fontname=font)
    graph.legend(loc='upper right')
    
    fig1 = graph.gcf()
    graph.show()
    graph.draw()
    
    fig1.savefig('avghit@'+str(N)+'.svg', dpi = 500)

