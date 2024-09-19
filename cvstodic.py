schema = "Nombre,Apellido,Edad,Mail"
row = "Emiliano,Billi,42,emiliano.billi@gmail.com"

class Str2Dic():
    def __init__(self , schemaStr,separator=","):
        self.schema=schemaStr.split(separator)
        self.separator=separator

    def convert(self, row):
        tmp=row.split(self.separator)
        if len(tmp)==len(self.schema):
            i=0
            d={} 
            while i<len(tmp):
                key=self.schema[i]
                val=tmp[i]
                d[key]=val
                i=i+1
            return d


o=Str2Dic(schema)
d=o.convert(row)   
print (d)            