import re
s="SELECT MIN(mc.note) AS production_note, MIN(t.title) AS movie_title, MIN(t.production_year) AS movie_year FROM company_type AS ct, info_type AS it, movie_companies AS mc, movie_info_idx AS mi_idx, title AS t WHERE ct.kind = 'production companies' AND it.info = 'top 250 rank' AND mc.note  not like '%(as Metro-Goldwyn-Mayer Pictures)%' and (mc.note like '%(co-production)%') AND t.production_year >2010 AND ct.id = mc.company_type_id AND t.id = mc.movie_id AND t.id = mi_idx.movie_id AND mc.movie_id = mi_idx.movie_id AND it.id = mi_idx.info_type_id;"
p=s.split('FROM')
x=p[1]
tables=x.split(' WHERE')
columns=tables[1]
tables=tables[0]
tables=tables.split(',')
columns=columns.split('AND')
p=".*\..*\=.*\..*"
q=[]
final_query=[]
for a in columns:
	m=re.search(p,a)
	if( not m):
		q.append(a)
print(tables)
print(q)
final= "SELECT COUNT(*) FROM"
for c in tables:
	p=c.split('AS ')
	p=p[1]+"."
	print(p)
	for d in q:
		if(d.startswith(" "+p)):
			query=final+c+" WHERE"+d+";"
			print(query)
			final_query.append(query)





		
	


