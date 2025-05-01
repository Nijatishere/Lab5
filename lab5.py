def tek_indeksli_ortalama(C):
 
    tek_indeksli_elements = C[1::2]
    
    if len(tek_indeksli_elements) == 0:
        return 0  
    return sum(tek_indeksli_elements) / len(tek_indeksli_elements)

C = [3, 7, 2, 5, 9, 1, 6, 8]

print(tek_indeksli_ortalama(C))
