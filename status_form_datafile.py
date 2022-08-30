from numpy import mean, std,median, min, max, percentile
lines = open("data_list.dat").readlines()
data = [float(x) for x in lines]
mu,sigma,med = mean(data),std(data),median(data)
min,max = min(data),max(data)
q1,q3 = percentile(data,25),percentile(data,75)
print('mu:%.2f,sigma:%.3f'%(mu,sigma))
print("min:%.2f,q1:%.2f,median:%.2f,q3:%.2f,max:%.2f"%(min,q1,med,q3,max))