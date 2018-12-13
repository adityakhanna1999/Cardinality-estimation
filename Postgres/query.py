import psycopg2
from config import config
final=[]
def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        with open("Query_list_POSTGRES.txt") as f:
            content = f.readlines()
            for i in content:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute(i)
                rows = cur.fetchone()
                print(rows)
                final.append(rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    get_vendors()
with open('POSTGRES_OUTPUT.txt', 'w') as f:
    for item in final:
        f.write("%s\n" % item)