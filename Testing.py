gameboard = ["|","S","|"," ","|","S","|"," ","|","S","|"," ","|","S","|", #0-15
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","U","|"," ","|","W","|"," ","|","R","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","R","|",
             "|","R","|"," ","|"," ","|"," ","|","U","|"," ","|"," ","|",
             "|"," ","|"," ","|","R","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","U","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|","W","|"," ","|","W","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","U","|"," ","|","U","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","W","|",
             "|","W","|"," ","|"," ","|"," ","|","R","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","R","|"," ","|","R","|"," ","|","U","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","R","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|","U","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|","W","|"," ","|","W","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","R","|"," ","|"," ","|"," ","|","R","|"," ","|","U","|",
             "|"," ","|"," ","|","W","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","U","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|","U","|"," ","|"," ","|",
             "|","W","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","R","|",
             "|"," ","|"," ","|","U","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","U","|",
             "|","W","|"," ","|"," ","|"," ","|","W","|"," ","|"," ","|",
             "|"," ","|"," ","|","R","|"," ","|"," ","|"," ","|","W","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","J","|"," ","|","J","|"," ","|","J","|"," ","|","J","|",
             ] 
#print(f'{"".j in(gameboard[0: ])}\n{"".join(g meboard[3:6])}\n{"".join(gameboard[6:9])}')
flag = 0
start = 0
end = 15
while flag != 35:
    print("".join(gameboard[start:end]))
    start += 15
    end += 15
    flag += 1