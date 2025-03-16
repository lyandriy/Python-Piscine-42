class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.f
        self.header_data
        self.lines

    def __enter__(self):
        try:
            self.f = open(self.filename, "r")
            line = f.readline()
            self.lines = []
            while line:
                self.lines.append(line.split(self.sep).strip())
                line = f.readline()
            size = 0
            if self.header:
                self.header_data = self.lines[0]
                size = len(self.lines[0])
                self.lines.pop(0)
            del self.lines[0:self.skip_top]
            del self.lines[self.skip_bottom:len(self.lines)]
            while line in self.lines:
                if size != len(line):
                    raise
        except ValueError:
            print("Bad file")
        
    def __exit__(self):
        if self.f:
            self.f.close()
        
    def getdata(self):
        if self.lines:
            return self.lines
        
    def getheader(self):
        if self.header_data:
            return self.header_data
        else:
            None