def analyze_numbers(numbers: list[float]) -> dict:
    sum=0
    min=max=numbers[0]
    for i in range(len(numbers)):
        sum+=numbers[i]
        if numbers[i]>max:
            max=numbers[i]
        if numbers[i]<min:
            min=numbers[i]
    total=sum
    average=sum/len(numbers)
    avg=round(average, 1)
    snum=sorted(numbers)
    dic={}
    dic['sorted']=snum
    dic['sum']=sum
    dic['average']=avg
    dic['min']=min
    dic['max']=max
    # print(snum)
    return dic

def print_dashboard(data: dict):
    for n, (key, value) in enumerate(data.items()):
        print(f"{n}. {key} → {value}")

#→
n=int(input('How many numbers to input?'))
loop=0
num=[]
while loop<n:
    num.append(float(input("Add number:")))
    loop+=1
d=analyze_numbers(num)
print_dashboard(d)
# analyze_numbers(num)
