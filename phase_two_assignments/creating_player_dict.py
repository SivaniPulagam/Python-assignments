player_dic = {}
n = int(input("Enter no.of players:"))
for i in range(1, n + 1):
    l = []
    pno = int(input("Enter player number:"))
    pname = input("Enter player name:")
    matches = int(input("Enter no of matches played:"))
    runs = int(input("Enter no of runs:"))
    wickets = int(input("Enter no of wickets:"))
    l.append(pname)
    l.append(matches)
    l.append(runs)
    l.append(wickets)
    player_dic[pno] = l
print(player_dic)
