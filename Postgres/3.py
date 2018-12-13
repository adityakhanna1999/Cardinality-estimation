actual=[]
predicted=[]
import csv
with open("POSTGRES_OUTPUT.txt") as f:
	    content = f.readlines()
	    for i in content:
	    	p=i.split('rows=')
	    	predicted_card=p[1].split(' ')
	    	print(predicted_card[0])
	    	predicted.append(predicted_card[0])
	    	actual_card=p[2].split(' ')
	    	print(actual_card[0])
	    	actual.append(actual_card[0])
zip(actual,predicted)
with open('FINAL_Cardinality.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(actual,predicted))