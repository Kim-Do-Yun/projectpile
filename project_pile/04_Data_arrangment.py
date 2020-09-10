from datetime import datetime

'''
학생의 정보를 자동 정리하고 해당 학생들의 성적을 평균내는 프로그램 입니다.

<프로그램 전>
Sam	27      A  B C  A  B
	Lee        18	A A  B  C  A
Kim    30 	B  C D  B   B
  Pack	28	C   C A D  A
 Lim	   	21	D  C  D  A B
  Jeong     22	B A   C  B A
Kang		20      B  B  C  C A

<프로그램 후>
Name    Age  Subject  Average
Sam	    27	A	B	C	A	B	3.2	
Lee	    18	A	A	B	C	A	3.4	
Kim	    30	B	C	D	B	B	2.4	
Pack	  28	C	C	A	D	A	2.6	
Lim	    21	D	C	D	A	B	2.2	
Jeong	  22	B	A	C	B	A	3.2	
Kang	  20	B	B	C	C	A	2.8	

Total Average : 2.83    (June 15, 2020)
'''

def readwrite(infile, outfile):
    nowdate = datetime.now()
    In = open(infile, "r", encoding="UTF-8")
    Out = open(outfile, "w", encoding="UTF-8")
    number = 0
    average = 0
    print("Name\tAge\t Subject\t\t\t\t Average")
    Out.write("Name\tAge\t Subject\t\t\t\t Average\n")
    for line in In:
      num = 0
      line = line.rstrip()
      word_line = line.split()
      for word in word_line:
        print(word, end="\t")
        Out.write(word + "\t")
        #print(word_line[0]+"\t\t\t"+word_line[1]+"\t\t"+word_line[2]+"\t"+word_line[3]+"\t")
      for word in word_line:
        if word == 'A':
          num += 4
        elif word == 'B':
          num += 3
        elif word == 'C':
          num += 2
        elif word == 'D':
          num += 1

        total = num / 5
        number += total
      print(total, end = "\t")
      Out.write(str(total) + "\t")
      print()
      Out.write("\n")
    
    average = number / 7

    Out.write("Total Average :"+ str(average) +"\t\t" +"("+nowdate.strftime("%B")+ nowdate.strftime("%d")+","+ nowdate.strftime("%Y")+")")


    In.close()
    Out.close()



    print("Total Average :", average ,"\t\t" "("+nowdate.strftime("%B"), nowdate.strftime("%d")+",", nowdate.strftime("%Y")+")")
    
readwrite("students.txt", "student_avg.txt")
