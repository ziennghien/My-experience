import statistics 
#1.2.1.	Statistics.mean(data):
A=[2,3,4,5,6]
x= statistics.mean(A)
print("Trung bình cộng mean():",x)
#1.2.2.	Statistics.fmean(data):
A=[2,3,4,5,6]
x= statistics.fmean(A)
print("Trung bình cộng fmean():",x)
#1.2.3.	Statistics.geometric_mean(data):
A=[54,24,36]
x= statistics.geometric_mean(A)
print("Trung bình nhân geometric_mean():",x)
#1.2.4.	Statistics.harmonic_mean(data,weights=none):
x= statistics.harmonic_mean([40,60],weights=[10,30])
print("Tốc độ trung bình (Số điều hòa bình quân) harmonic_mean():", x)
#1.2.5.	Statistics.median(data):
A=[2,4,3,6,5]
x= statistics.median(A)
print("Trung vị median():",x)
#1.2.6.	Statistics.median_low(data):
A={'a','b','c','d','e','g'}
x= statistics.median_low(A)
print("Trung vị thấp median_low(): ",x)
#1.2.7.	Statistics.median_high(data):
A={'a','b','c','d','e','g'}
x= statistics.median_high(A)
print("Trung vị cao median_high():",x)
#1.2.8.	Statistics.median_grouped(data,interval=1):
A=[1, 3, 3, 5, 7]
x= statistics.median_grouped(A)
print("Trung vị median_grouped():",x)
#1.2.9.	Statistics.mode(data):
A=[1,3,3,3,5,7,7,7]
x= statistics.mode(A)
print("Yếu vị mode():",x)
#1.2.10.Statistics.multimode(data):
A=[1,3,3,3,5,7,7,7]
x= statistics.multimode(A)
print("Danh sách yếu vị:",x)
#1.2.11.Statistics.quantiles(data,*,n=4,method=’exclusive’):
A=[1,3,5,6,7,2,4]
x= statistics.quantiles(A)
print("Tứ phân vị quantiles():",x)
#1.2.12.Statistics.pstdev(data, mu=None):	
A=[1,3,5,6,7,2,4]
x= statistics.pstdev(A)
print("Độ lệch chuẩn pstdev():",x)
#1.2.13.Statistics.pvariance(data, mu=None):	
A=[1,3,5,6,7,2,4]
x= statistics.pvariance(A)
print("Phương sai pvariance():",x)
#1.2.14.Statistics.stdev(data, xbar=None):	
A=[1,3,5,6,7,2,4]
x= statistics.stdev(A)
print("Độ lệch chuẩn mẫu stdev(): ",x)
#1.2.15.Statistics.variance(data, xbar=None):
A=[1,3,5,6,7,2,4]
x= statistics.variance(A)
print("Phương sai mẫu variance():",x)
#1.2.16.Statistics.covariance(x,y,/):	
A=[1,2,3,4,5,6]
B =[3,4,5,6,7,8]
x= statistics.covariance(A,B)
print("Hiệu phương sai giữa A và B covariance():",x)
#1.2.17.Statistics. correlation(x, y, /, *, method='linear'):
A=[1,2,3,4,5,6]
B =[3,4,5,6,7,8]
x= statistics.correlation(A,B)
print("Hệ số tương quan giữa A và B correlation():",x)
#1.2.18.Statistics. linear_regression(x, y, /, *, proportional=False):
B =[1,6,7,3,4,9]
x,y= statistics.linear_regression(A,B,proportional='True')
print("Hệ số góc: ",x)
print("Độ lệch:",y)













