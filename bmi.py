import numpy as np
from matplotlib import pyplot as plt

#키와 몸무게를 이용해 bmi어레이 만들기
def bmi_compute(wt,ht):
    bmi=wt/((ht/100)*(ht/100))

    return bmi


#40~90사이로 랜덤한 학생 몸무게 어레이 만들기
wt=np.random.randint(40,91,size=100)

#140~200 사이로 랜덤한 학생 키 어레이 만들기 
ht=np.random.randint(140,201,size=100)


#bmi생성
bmi=bmi_compute(wt,ht)
bmi=np.round(bmi,1)

#bmi 어레이 출
print("BMI Array>>\n")
print(bmi,"\n")

#bmi 어레이 첫번째 부터 10개 출력
print("first 10 elements of the BMI>>\n")
print(bmi[0:10])

#bmi 레벨별 개수 구하는 함수.
def bmi_count(bmi):
    count1=0
    count2=0
    count3=0
    count4=0

    for i in range(len(bmi)):
        if bmi[i]<18.5:
            count1 = count1+1
        elif 18.5<=bmi[i]<25.0:
            count2 = count2+1
        elif 25.0<=bmi[i]<30.0:
            count3 = count3+1
        else:
            count4 = count4+1
    
    
    bmi_count=[count1,count2,count3,count4]
        
    return bmi_count

category=['underweight','healthy','overweight','obese']
bmi_count = bmi_count(bmi)

#각 레벨별 bmi,몸무게, 키 저장
underweight_bmi = []
healthy_bmi = []
overweight_bmi = []
obese_bmi = []

underweight_weight = []
healthy_weight = []
overweight_weight = []
obese_weight = []

underweight_height = []
healthy_height = []
overweight_height = []
obese_height = []


for i in range(len(bmi)):
    if bmi[i]<18.5:
        underweight_bmi.append(bmi[i])
        underweight_weight.append(wt[i])
        underweight_height.append(ht[i])
        
    elif 18.5<=bmi[i]<25.0:
        healthy_bmi.append(bmi[i])
        healthy_weight.append(wt[i])
        healthy_height.append(ht[i])
        
    elif 25.0<=bmi[i]<30.0:
        overweight_bmi.append(bmi[i])
        overweight_weight.append(wt[i])
        overweight_height.append(ht[i])
        
    else:
        obese_bmi.append(bmi[i])
        obese_weight.append(wt[i])
        obese_height.append(ht[i])

#Box Plot_weight
plotData=[underweight_weight,healthy_weight,overweight_weight,obese_weight]
plt.boxplot(plotData)
plt.xlabel('BMI level')
plt.ylabel('weight')
plt.title('Box_Plot(weight)')
plt.show()

#Box Plot_height
plotData=[underweight_height,healthy_height,overweight_height,obese_height]
plt.boxplot(plotData)
plt.xlabel('BMI level')
plt.ylabel('height')
plt.title('Box_Plot(height)')
plt.show()

#histogram_weight
plt.hist([underweight_weight,healthy_weight,overweight_weight,obese_weight],bins=4)
plt.title('BMI histogram(weight)')
plt.xlabel('weight')
plt.ylabel('number of student')
plt.legend(category)
plt.show()

#histogram_height
plt.hist([underweight_height,healthy_height,overweight_height,obese_height],bins=4,
         label=category)
plt.title('BMI histogram(height)')
plt.xlabel('height')
plt.ylabel('number of student')
plt.legend(category)
plt.show()


#pie chart
plt.pie(bmi_count,labels=category,autopct='%1.2f%%')
plt.title('BMI Pie Chart')
plt.show()

#scatter plot
stNum=[]
for x in range(100):
    stNum.append(x)
    
plt.scatter(stNum,wt,color='r')
plt.scatter(stNum,ht,color='b')
plt.legend(['weight','height'])
plt.title('Weight & Height Scatter Plot')
plt.show()

