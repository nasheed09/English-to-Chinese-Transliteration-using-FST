# FST Program  for chinese-Eng transliteration for borrowed words
from nltk.nltk_contrib.fst.fst import *

class myFST(FST):    
    def recognize(self, iput, oput):
        self.inp = list(iput)
        self.outp = list(oput)    
        if list(oput) == f.transduce(list(iput)):       
            return True
        else:
            return False

f = myFST('example')
# first add the states in the FST
for i in range(1,6):
    f.add_state(str(i)) # add states '1' .. '5'

# add one initial state
f.initial_state = '1' # -> 1

# add all transitions
f.add_arc('1', '2', ['vi'], ['wei'])
f.add_arc('1', '2', ['la'], ['na'])
f.add_arc('1', '2', ['mo'], ['mo'])
f.add_arc('1', '2', ['ti'], ['ti'])
f.add_arc('1', '2', ['bun'], ['beng'])
f.add_arc('1', '2', ['las'], ['lais'])
f.add_arc('1', '2', ['hac'], ['hei'])

f.add_arc('2', '3', ['ta'], ['ta'])
f.add_arc('2', '3', ['tte'], ['tie'])
f.add_arc('2', '3', ['cha'], ['ka'])
f.add_arc('2', '3', ['ra'], ['la'])
f.add_arc('2', '3', ['gee'], ['ji'])
f.add_arc('2', '3', ['er'], ['he'])
f.add_arc('2', '3', ['ker'], ['ke'])

f.add_arc('3', '4', ['min'], ['ming'])
f.add_arc('3', '4', ['mi'], ['mi'])

f.add_arc('4', '5', ['su'], ['su'])

# add final/accepting state(s)
f.set_final('3')
f.set_final('4')
f.set_final('5')



inps = ["vi ta min", "la tte", "mo cha", "ti ra mi su", "bun gee", "las er", "hac ker"]
outs = ["wei ta ming", "na tie", "mo ka", "ti la mi su", "beng ji", "lais he", "hei ke"]


file = open("Chn-trans.dat", 'a')
for i in range(len(inps)):
 	word_in = inps[i].split()
 	word_out = outs[i].split()
 	if f.recognize(word_in, word_out):
 		print("accepted")
 		print(word_in + " : " + word_out)
 		file.write("\n")
 		for a,b in zip(word_in, word_out):
 			file.write(a+" --> " + b + "\n")
 	else:
 		print("rejected")
 		print(word_in + " : " + word_out)

x = input("Enter Sample to test, make sure it's separated by space\nThe Word: ")
disp = FSTDemo(f)
disp.transduce(x.split())
disp.mainloop()
