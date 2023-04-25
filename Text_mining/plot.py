import matplotlib.pyplot as plt
import numpy as np

def read_csv_file(csvfilename):
    f = open(csvfilename,encoding= 'utf-8')
    top_lines = f.readlines()
    top_pairs = []
    for l in top_lines:
        toks=l.split(',')
        top_pairs.append((toks[0],int(toks[1])))
    return top_pairs

def make_plot(top_pairs,outfilename,title):
    labels = [x[0] for x in top_pairs [:10]]
    counts = [int(x[1])for x in top_pairs[:10]]
    label_pos = np.arange(len(labels))

    plt.barh(labels,counts,align='center',alpha=0.5,color="red")
    plt.yticks = (label_pos,labels)
    plt.xlabel('count')
    plt.title(title)
    plt.savefig(outfilename)
    plt.close()

def get_sum(nums):
    sum = 0
    for n in nums:
        sum+=n
    return sum

def normalize(top_pairs):
    sum = get_sum([tp[1] for tp in top_pairs])
    return [(tp[0],tp[1]/sum * 100)for tp in top_pairs]

def make_dict(top_pairs):
    dict = {}
    for w,p in top_pairs:
        dict[w]= p
    return dict

def compare_plots(top_pairs1,top_pairs2,outfilename,title):
    norm_top_pairs1 = normalize(top_pairs1)
    norm_top_pairs2 = normalize(top_pairs2)
    dic_top_pairs2=make_dict(norm_top_pairs2)

    stats = []
    for w,p1 in norm_top_pairs1[:10]:
        p2 = 0
        if w in dic_top_pairs2:
            p2= dic_top_pairs2[w]
        stats.append((w,p1,p2))
        
    
    labels=[s[0] for s in stats[:10]] 
    label_pos=np.arange(0,len(labels))
    nrm_count1=[s[1] for s in stats[:10]]
    nrm_count2=[s[2] for s in stats[:10]]
    
    
    plt.bar(labels,nrm_count1,align='center',width= 0.4,color="hotpink")
    plt.bar(labels,nrm_count2,align='center',width= 0.4,color="green")
    plt.xticks = (label_pos,labels)
    plt.ylabel('percent')
    plt.title(title)
    plt.legend()
    plt.savefig(outfilename)
    plt.close()




mtr_stats = read_csv_file("mtr.result.csv")
make_plot(mtr_stats,"mtr.jpg","meteora")

hbt_stats = read_csv_file("hbt.result.csv")
make_plot(hbt_stats,"hbt.jpg","hybrid theory")

compare_plots(mtr_stats,hbt_stats,"mtr_hbt.jpg","mtr-->hbt")
compare_plots(hbt_stats,mtr_stats,"hbt_mtr.jpg","hbt-->mtr")

