import csv

class RedAlliance():
    def __init__(self):
        self.csv_match_data = [] #Combined data of all matches
        self.csv_pit_data = [] #Combined data of all pits
        self.csv_match_sources = [] #List of all csv sources for above matches
        self.csv_pit_sources = [] #List for pits
        self.match_header = [] #List of headings for matches
        self.pit_header = [] #List of headings for pits
        
    def add_match_source(self, csv_path):
        #This adds data to the main data set in this form:
        # 0 |{"Header1": value1, "Header2": value4, ...}
        # 1 |{"Header1": value2, "Header2": value5, ...}
        # 2 |{"Header1": value3, "Header2": value6, ...}
        # ..|{..}
        if type(csv_path) is str:
            self.csv_match_sources.append(csv_path) #Add to list of sources
            file = csv.reader(open(csv_path), delimiter=",")
            this_header = next(file)
            if not self.match_header: #If no header exists yet
                self.match_header = this_header #This becomes the official header
            if this_header == self.match_header: #If we have matching headers
                for row in file:
                    header_index = 0; #Used to properly mark the table structure
                    tempRow = {} #Clear the temp row for the next one
                    for cell in row:
                        tempRow[self.match_header[header_index]] = cell #Add each cell onto that row
                        header_index += 1
                    self.csv_match_data.append(tempRow) #Add that row onto the main data
            else:
                raise AttributeError("RedAlliance: The headers of the first given match file \
                                        and the file " + csv_path + " do not match.")
        else:
            raise TypeError("RedAlliance: csv_path must be a string.")
        
    def add_pit_source(self, csv_path):
        if type(csv_path) is str:
            self.csv_pit_sources.append(csv_path) #Add to list of sources
            file = csv.reader(open(csv_path), delimiter=",")
            this_header = next(file)
            if not self.pit_header: #If no header exists yet
                self.pit_header = this_header #This becomes the official header
            if this_header == self.pit_header: #If we have matching headers
                tempRow = [] #Row for adding rows to main data
                for row in file:
                    header_index = 0; #Used to properly mark the table structure
                    tempRow = {} #Clear the temp row for the next one
                    for cell in row:
                        tempRow[self.pit_header[header_index]] = cell #Add each cell onto that row
                        header_index += 1
                    self.csv_pit_data.append(tempRow) #Add that row onto the main data
            else:
                raise AttributeError("RedAlliance: The headers of the first given match file \
                                        and the file " + csv_path + " do not match.")
        else:
            raise TypeError("RedAlliance: csv_path must be a string.")
    
    def sort_matches_by(self, column_name):
        if column_name in self.match_header:
            self.csv_match_data = sorted(self.csv_match_data, key=lambda row:  0 if not int(row[column_name]) else int(row[column_name]))
        else:
            raise AttributeError("RedAlliance: column_name must be a valid match header.")
    
    def sort_pits_by(self, column_name):
        if column_name in self.pit_header:
            self.csv_pit_data = sorted(self.csv_pit_data, key=lambda row: int(row[column_name]))
        else:
            raise AttributeError("RedAlliance: column_name must be a valid pit header.")
    
    def write_matches_to_html_table(self, html_path):
        html_file = open(html_path, 'w')
        html_file.truncate(0)
        html_file.write("<html><body><table border='2'>")
        for cell in self.match_header:
            html_file.write("<th>" + str(cell) + "</th>")
        for row in self.csv_match_data: #Goes through each row
            html_file.write("<tr>")
            for cell in row:
                html_file.write("<td>" + row[cell] + "</td>")
            html_file.write("</tr>")
        html_file.write("</table></body></html>")
        html_file.close()
        
    def write_pits_to_html_table(self, html_path):
        html_file = open(html_path, 'w')
        html_file.truncate(0)
        html_file.write("<html><body><table border='2'>")
        for cell in self.pit_header:
            html_file.write("<th>" + str(cell) + "</th>")
        for row in self.csv_pit_data: #Goes through each row
            html_file.write("<tr>")
            for cell in row:
                html_file.write("<td>" + row[cell] + "</td>")
            html_file.write("</tr>")
        html_file.write("</table></body></html>")
        html_file.close()
        
scouter = RedAlliance()
scouter.add_match_source("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Development\\Python Development Repository\\Development Repo\\Scouting Sheet\\raw_scouting_data.csv")
scouter.add_pit_source("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Development\\Python Development Repository\\Development Repo\\Scouting Sheet\\raw_pit_scouting_data.csv")

scouter.sort_matches_by("Team Number")
scouter.sort_pits_by("Top speed(s) in feet per second (fps)")
scouter.write_matches_to_html_table("C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Development\\Python Development Repository\\Development Repo\\Scouting Sheet\\datatable.html")


