class Solution(object):
    def tictactoe(self,moves:list[list[int]])->str:
        a,b=[0]*8,[0]*8
        for index in range(len(moves)):
            row,col=moves[index]
            if index%2==0:
                player=a
            else:
                player=b
            player[row]+=1
            player[col+3]+=1
            if row==col:
                player[6]+=1
            if row==2-col:
                player[7]+=1
        for i in range(len(a)):
            if a[i]==3:
                return "A"
            if b[i]==3:
                return "B"
        if len(moves)==9:
            return "Draw"
        else:
            return "Pending"
