fn="test.csv"
data=[line.strip() for line in open(fn,"r")]
#print(data[0])
data2=data[1:]

index_tmp=data[0].split(",")
freq_index=index_tmp[0]
block_index=index_tmp[1]
clk_index=index_tmp[2]

freq_list=[tmp.split(",")[0] for tmp in data2]
freq_list_uni=list(set(freq_list))
block_list=[tmp.split(",")[1] for tmp in data2]
clk_list=[tmp.split(",")[2] for tmp in data2]

index_list=[]
for j in range(len(freq_list_uni)):
    j1=freq_list_uni[j]
    j_tmp=[i for i,x in enumerate(freq_list) if x == j1 ]
    index_list.append([j1,j_tmp])
print(index_list)

    