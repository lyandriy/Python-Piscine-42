class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.f = None
        self.header_data = None
        self.lines = None

    def __enter__(self):
        try:
            self.f = open(self.filename, "r")
            line = self.f.readline()
            self.lines = []
            while line:
                l  = line.split(self.sep)
                l = [x.strip() for x in l]
                self.lines.append(l)
                line = self.f.readline()
            size = 0
            if self.header:
                self.header_data = self.lines[0]
                size = len(self.lines[0])
                self.lines.pop(0)
            del self.lines[0:self.skip_top]
            if self.skip_bottom > 0:
                if self.skip_bottom < self.skip_top:
                    self.skip_bottom = self.skip_top
                del self.lines[-self.skip_bottom:]
            for linee in self.lines:
                if size != len(linee):
                    raise ValueError("Bad file")
        except ValueError as e:
            print(f"Bad file: {e}")
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if self.f:
                self.f.close()
        except Exception as e:
            print(f"Error al cerrar el archivo: {e}")
            return False
        return True
        
    def getdata(self):
        if self.lines:
            return self.lines
        
    def getheader(self):
        return self.header_data