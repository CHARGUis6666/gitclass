def import_data(filename):
    data = open(filename, 'r')
    X = []
    y = []
    attribute = []
    count = 0
    # cleaning each row
    datalines = data.readlines()
    for line in data:
        line = line.split(',')
        for element in line:
            count +=1
            if element == "?":
                element = "NaN"
            else:
                element = element
            if count < 280:
                attributes.append(element)
            if count == 280:
                y.append(element)
                X.append(attribute)
                attributes = []
                count = 0   #reset
            
       
    return X, y
                
        
 