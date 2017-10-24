import csv

csv_file = csv.reader(open("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Development\\Python Development Repository\\Development Repo\\Scouting Sheet\\raw_scouting_data.csv"), delimiter="," )
print("READER_STRUCTURE")
data = [] #Data accessible by data[row_index]['column name']
temporary_row = {} #Dictionary used to build rows before appending them
header = next(csv_file) #The header is the title of the columns
for row in csv_file:
    correlator_index = 0
    for cell in row:
        temporary_row[header[correlator_index]] = cell
        #^ Makes key-value pairs like 'team number': 3 for each column in each row
        correlator_index += 1
    data.append(temporary_row)
    temporary_row = {}
#Data is accessible like this now:
print(data[0]['Timestamp']) #Prints the first timestamp



#SORTING
#We need to change the order of the 'data' list based on the value of data[i]['Team Number']
org_data = sorted(data, key=lambda row: int(row['Match Number']))
for row in org_data:
    print(row)
def to_html_table(data, header, html_path):
    html_file = open(html_path, 'w')
    html_file.truncate(0)
    html_file.write("<html><body><table border='2'>")
    for cell in header:
        html_file.write("<th>" + str(cell) + "</th>")
    for row in data: #Goes through each row
        html_file.write("<tr>")
        for cell in row:
            html_file.write("<td>" + row[cell] + "</td>")
        html_file.write("</tr>")
    html_file.write("</table></body></html>")
    html_file.close()
to_html_table(org_data, header, "C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Development\\Python Development Repository\\Development Repo\\Scouting Sheet\\datatable.html")