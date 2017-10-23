import csv

def to_html_table(data, header, html_path):
    html_file = open(html_path, 'w')
    html_file.truncate(0)
    html_file.write("<html><body><table border='2'>")
    for cell in header:
        html_file.write("<th>" + str(header[cell]) + "</th>")
    for row in data: #Goes through each row
        html_file.write("<tr>")
        for cell in row:
            html_file.write("<td>" + row[cell] + "</td>")
        html_file.write("</tr>")
    html_file.write("</table></body></html>")
    html_file.close()
