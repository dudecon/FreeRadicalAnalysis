files = ("Chapter Summaries",
        "Character Summaries",
        "Writing Style",
        "Primary Tropes")

keys = ("**Summary:**",
        "**Character Summaries:**",
        "**Writing Style:**",
        "**Primary Tropes:**")

f = open("Plot Analysis.txt", "r")
data = f.read()
f.close()

#print(len(data), data[:500])
startpos = 0
endpos = 0
sections = ["Summary:\n","Characters:\n","Style:\n","Tropes:\n",]
i = 0
while True:
    secti = i % len(keys)
    thissecti = keys[secti]
    nextsecti = keys[(i + 1) % len(keys)]
    startpos = data.find(thissecti,startpos) + len(thissecti)
    endpos = data.find(nextsecti,endpos)
    sections[secti] += data[startpos:endpos]
    if endpos == -1: break
    else: i += 1
    
for i in range(len(files)):
    f = open(files[i]+".txt", "w")
    f.write(sections[i])
    f.close()
