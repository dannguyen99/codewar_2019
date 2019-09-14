def digitalNumber(lightStatus):
    lights = {}
    table = {"****.**.**.****": 0, "..*..*..*..*..*": 1, "***..*****..***": 2,
             "***..****..****": 3, "*.**.****..*..*": 4, "****..***..****" :5, "****..****.****": 6,
             "***..*.**..*..*" :7, "****.*****.****": 8, "****.****..****": 9}
    for status in lightStatus:
        for i in range(0, len(status), 3):
            if i not in lights:
                lights[i] = []
                lights[i].append(status[i:i + 3])
            else:
                lights[i].append(status[i:i + 3])
    possibles = []
    for i in lights:
        possibles.append(''.join(lights[i]))
    result =''
    for i in possibles:
        result += str(table[i])
    return result


print(digitalNumber(["****.*","*.**.*","*.****","*.*..*","***..*"]))
