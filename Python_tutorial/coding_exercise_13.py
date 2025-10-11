row_1=['😀','😀','😀']
row_2=['😀','😀','😀']
row_3=['😀','😀','😀']
matrix=[row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}")
position=input("Enter the position where you want to hide money:")
#print(matrix)
row_number=int(position[0])
column_number=int(position[1])
a=int(row_number-1)
b=int(column_number-1)
matrix[a][b]="X"
print(f"{row_1}\n{row_2}\n{row_3}")

