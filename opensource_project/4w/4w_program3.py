instr, outstr = "", ""
count, i = 0, 0

instr = input("문자열을 입력하세요 : ")
count = len(instr)


for i in range(0, count) :
    outstr += instr[count - (i+1)]

print("내용을 거꾸로 출력 --> %s" % outstr)

