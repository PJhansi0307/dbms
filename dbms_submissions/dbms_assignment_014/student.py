class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass
"""def write_data(sql_query):
    	import sqlite3
    	connection = sqlite3.connect("students.sqlite3")
    	crsr = connection.cursor() 
    	crsr.execute("PRAGMA foreign_keys=on;") 
    	crsr.execute(sql_query) 
    	connection.commit() 
    	connection.close()
"""
def read_data(sql_query):
    	import sqlite3
    	connection = sqlite3.connect("students.sqlite3")
    	crsr = connection.cursor() 
    	crsr.execute(sql_query) 
    	ans= crsr.fetchall()  
    	connection.close() 
    	return ans

class Student:

    def __init__(self,name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
     
    @classmethod
    def filter(cls,**kwargs):
        objects_list=[]
        operator={'lt' : '<', 'lte' : '<=', 'gt' : '>', 'gte' : '>=', 'neq' : '!=', 'in' : 'in'}
        
        for key, value in kwargs.items():
                    
            keys = key
            value=value
            keys = keys.split('__')
            if keys[0] not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField 
            
            if len(keys) == 1:
                sql_query= f" {key} = '{value}'"
                    
            elif keys[1] == 'in':
                sql_query = f"{keys[0]} {operator[keys[1]]} {tuple(value)}"
                    
            elif keys[1] == 'contains':
                sql_query = f"{keys[0]} like '%{value}%'"
                    
            else:    
                sql_query = f"{keys[0]} {operator[keys[1]]} '{value}'"
                
            objects_list.append(sql_query)
                    
        mul_conditions = " and ".join(objects_list)      
        sql_query = " " + mul_conditions
        return sql_query
    @classmethod
    def avg(self,field,**kwargs):
        if field not in('name','age','score','student_id'):
            raise InvalidField
        else:
            if len(kwargs)==0:
                r='select avg({}) from Student'.format(field)
                m=read_data(r)
            else:
                q=Student.filter(**kwargs)
                r='select avg({}) from Student where {}'.format(field,q)
                m=read_data(r)
        return m[0][0]
    @classmethod
    def min(self,field,**kwargs):
        if field not in('name','age','score','student_id'):
            raise InvalidField
        else:
            if len(kwargs)==0:
                r='select min({}) from Student'.format(field)
                m=read_data(r)
            else:
                q=Student.filter(**kwargs)
                r='select min({}) from Student where {}'.format(field,q)
                m=read_data(r)
        return m[0][0]
    @classmethod
    def max(self,field,**kwargs):
        if field not in('name','age','score','student_id'):
            raise InvalidField
        else:
            if len(kwargs)==0:
                r='select max({}) from Student'.format(field)
                m=read_data(r)
            else:
                q=Student.filter(**kwargs)
                r='select max({}) from Student where {}'.format(field,q)
                m=read_data(r)
        return m[0][0]
    @classmethod
    def count(cls,field=None,**kwargs):
        if field==None:
            r="select count(*) from student"
        elif field not in ('student_id','name','age','score'):
            raise InvalidField
        elif len(kwargs)==0:
                r="select count({}) from Student".format(field)
        else:
                q=Student.filter(**kwargs)
                r="select count({}) from Student where {}".format(field,q)
        m=read_data(r)
        return m[0][0]
    @classmethod
    def sum(self,field,**kwargs):
        if field not in('name','age','score','student_id'):
            raise InvalidField
        else:
            if len(kwargs)==0:
                r='select sum({}) from Student'.format(field)
                m=read_data(r)
            else:
                q=Student.filter(**kwargs)
                r='select sum({}) from Student where {}'.format(field,q)
                m=read_data(r)
        return m[0][0]
        
        
        
#avg_age = Student.avg('age')
#avg_age = Student.avg('age', age__gt=18)
#avg_age = Student.avg('age', age__gt=18, age__lt=21)
#min_age = Student.min('age')
#print(min_age)