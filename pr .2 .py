# Mike has made the decision to organise a competition. The contest is that mike has a word withhim written 
#on the tab and if the participants names contain both the last two letters of the wordhe has , he will affirm
#and present the gift after saying it True. Otherwise he will say False . Mike needs your assistance to 
# detrmine the winners.

a = str(input(""))
b = str(input(""))
if a[-1:-3] in b:
    print("True")
else:
    print("False")