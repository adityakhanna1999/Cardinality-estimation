import re
import os
files=[]
su=0
for i in os.listdir("job/"):
    if i.endswith('.txt'):
        files.append(i)
        su+=1
# print(files)
# print(su)
count1=0
final_query=[]
for f in files:
	x="job/"+f
	count=0
	with open(x, 'r') as myfile:
		s = myfile.read()
		# s="SELECT MIN(t.title) AS movie_title FROM company_name AS cn, keyword AS k, movie_companies AS mc, movie_keyword AS mk, title AS t WHERE cn.country_code ='[de]' AND k.keyword ='character-name-in-title' AND cn.id = mc.company_id AND mc.movie_id = t.id AND t.id = mk.movie_id AND mk.keyword_id = k.id AND mc.movie_id = mk.movie_id;"
		p=s.split('FROM')
		x=p[1]
		tables=x.split(' WHERE')
		columns=tables[1]
		tables=tables[0]
		tables=tables.split(',')
		columns=columns.split('AND')
		p=".*\..*\=.*\..*"
		q=[]
		for a in columns:
			m=re.search(p,a)
			if( not m):
				q.append(a)
		
		final= "SELECT COUNT(*) FROM"
		for c in tables:
			p=c.split('AS ')
			p=p[1]+"."
			for d in q:
				if(d.startswith(" "+p)):
					query=final+c+" WHERE"+d+";"
					# print(query)
					count+=1
					final_query.append(query)
# print(count)
#removing duplicates
s=[]
for i in final_query:
	if i not in s:
		s.append(i)
		count1+=1
# print(count1)
print(s)
with open('Query_list.txt', 'w') as f:
    for item in s:
        f.write("%s\n" % item)
