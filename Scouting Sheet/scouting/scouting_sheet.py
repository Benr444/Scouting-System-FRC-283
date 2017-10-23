import csv

csv_file = csv.DictReader(open("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Workspace\\Scouting Sheet\\raw_scouting_data.csv"))
html_file = open("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Workspace\\Scouting Sheet\\datatable.html", 'w')
html_file.truncate(0)
html_file.write("<html><body><table border='2'>")
#Break baseline,Fuel scored low boiler,Fuel scored high boiler,Gear placed on spike,Additional comments,Primary Scoring Location,Fuel Accumulated,Gears placed on spike,How is fuel loaded into the robot?,How are gears loaded into the robot?,Climbing,Additional Comments?,Pilot data
for row in csv_file: #Goes through each row
    html_file.write("<tr>")
    for cell in row:
        html_file.write("<td>" + row[cell] + "</td>")
    html_file.write("</tr>")
html_file.write("</table></body></html>")
html_file.close()
