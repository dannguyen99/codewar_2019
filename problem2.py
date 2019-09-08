from datetime import datetime


def attackList(accessList, m, n):
    users = {}
    result = []
    for i in accessList:
        user = i.split()[1]
        date = datetime.strptime(i.split()[0], '%y%m%d%H%M%S')
        if (user) not in users:
            users[user] = []
            users.get(user).append(date)
        else:
            users.get(user).append(date)
    for j in users:
        accesses = sorted(users.get(j))
        # print(accesses)
        for i in accesses:
            access = 1
            print([element for element in accesses if element is not i])
            for k in [element for element in accesses if element is not i]:
                # print(abs((accesses[i] - accesses[k]).total_seconds()/60) == m)
                if abs((i - k).total_seconds()/60) <= m:
                    access += 1
            if access >= n:
                result.append(j)
                break
    return sorted(result)


accessList = ["190920175400 vietcv", "190920175600 vietcv"]
m = 2
n = 2
date1 = datetime.strptime('190919175400', '%y%m%d%H%M%S')
date2 = datetime.strptime('190919175400', '%y%m%d%H%M%S')
print(date1 is date2)
print((date2 - date1).total_seconds()/60 < 2)
print(attackList(["190920175600 vietcv", "190920175600 vietcv", "190920175600 vietcv"], 0, 3))
