import sqlparse as sp

sql = "select column1, column2 from schema1.name1"
sqlFormatted = sp.format(sql, reindent=True, keyword_case ='upper')
parsed = sp.parse(sqlFormatted)
# print(sqlParsed[0])
print(parsed[0].tokens)
stmt = parsed[0]
columns = []
for token in stmt.tokens:
    if isinstance(token, IdentifierList) :
        for identifier in token.get_identifiers():
            columns.append(str(identifier))
print(columns)
