from operator import itemgetter

class OS():
    def __init__(self, ID, Name, Version):
        self.ID = ID
        self.Name = Name
        self.Version = Version
#OS description end

class PC():
    def __init__(self, ID, Name, MAC, OS_ID):
        self.ID = ID
        self.Name = Name
        self.MAC = MAC
        self.OS_ID = OS_ID
#PC description end

class PC_OS():
    def __init__(self, PC_ID, OS_ID):
        self.PC_ID = PC_ID
        self.OS_ID = OS_ID
#ClassComb description end

os = [
    OS(1, "Linux", "1.0"),
    OS(2, "Debian", "2.0"),
    OS(3, "Windows 10", "9.9.9"),
    OS(4, "Windows 8.1", "6.6.6"),
    OS(5, "Windows 7", "7.9"),
    OS(6, "Windows XP", "14.H8"),
    OS(7, "Windows 98", "19.98"),
    OS(8, "Lollipop", "5.3"),
    OS(9, "Marshmallow", "6.0"),
    OS(10, "Android", "1.0")
]

pc = [
    PC(1,"MSI Aegis 3 8RC-206RU (9S6-B91811-206)","DB:C3:A5:1C:40:24",1),
    PC(2, "Lenovo Legion C530-19ICB (90JX003XRS)", "93:0F:2C:06:6F:E5",2),
    PC(3, "MSI Trident A 8SD-079RU (9S6-B92611-079)","5C:A6:59:73:88:C4",3),
    PC(4, "HP 880-111ur (3EQ89EA)","DF:A7:21:48:DA:B8",4),
    PC(5, "ASUS ROG Strix GL12CS-RU003T","FA:7D:5F:3F:F3:B8",5),
    PC(6, "Lenovo Legion T530-28APR (90JY000VRS)","2C:D6:9A:E1:DF:3E",6),
    PC(7, "Lenovo Legion T730-28ICO (90JF0062RS)","09:E7:1A:EF:72:E5",7),
    PC(8, "Acer Predator Orion 3000 (DG.E14ER.002)","E2:17:F7:7C:38:50",8)
]

comb = [
    PC_OS(6,1),
    PC_OS(6,10),
    PC_OS(2,3),
    PC_OS(2,4),
    PC_OS(7,6),
    PC_OS(7,5),
    PC_OS(7,10)
]

def main():
    # Соединение данных один-ко-многим
    one_to_many = [(i.Name, i.Version, j.Name, j.MAC) for i in os for j in pc if j.OS_ID == i.ID]
    
    print()
    print('Задание Б1')
    print(sorted(one_to_many, key=itemgetter(2)))

    # Соединение данных один-ко-многим 
    one_to_many_2 = []
    for i in os:
        counter = 0
        for j in pc:
            if i.ID == j.OS_ID:
                counter += 1
        one_to_many_2.append((i.Name, counter))
    print()
    print('Задание Б2')
    print(sorted(one_to_many_2, key=itemgetter(1)))

    # Много-ко-многим
    many_to_many = {}
    for i in comb:
        if 'Lenovo' in pc[i.PC_ID-1].Name:
            if pc[i.PC_ID-1].Name not in many_to_many.keys():
                 many_to_many[pc[i.PC_ID-1].Name] = set()
            many_to_many[pc[i.PC_ID-1].Name].add(os[i.OS_ID-1].Name)

    print()
    print('Задание Б3')
    print(many_to_many)

if __name__ == '__main__':
    main()