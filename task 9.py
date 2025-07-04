def read_marks_file():
   filename=input("Enter your file name: ")
   with open(filename, 'r') as file:
        dic={}
        count=0

        for line in file:
            line=line.replace("\n","")
            part=line.split(",")
            try:
                if part[0]=="" or part[1]=="" or not int(part[1]):
                    raise ValueError()
                dic[part[0]]=int(part[1])
            except ValueError:
                count+=1
                continue
        return (dic, count)

def print_summary(marks_dict: dict, miss: int):
    average=0
    for keys, values in marks_dict.items():
        print(f'{keys} → {values} | ',end="")
        average+=values
    average/=len(marks_dict)
    print(f"Average: {average:.1f}")
    print(f'Skipped {miss} invalid entries.')

dictionary, missing=read_marks_file()
print_summary(dictionary, missing)

            
         