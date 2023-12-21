class Rolnik:
    filename = "class_fields.txt"
    fields = []
    farmer = ""
    
    def save(self):
        f_fields = self.format_fields_data(self.fields)
        self.write_fields_data_to_file(self, self.farmer, f_fields)

    def write_fields_data_to_file(self, farmer, fields_data):
        with open(self.filename, "a") as file:
            file.write(f"{farmer}; {fields_data}\n")

    def format_fields_data(fields):
        # [(20,50), (44,80)]
        return ", ".join([(f"{l}x{w}") for l,w in fields])


rolnik = Rolnik()
rolnik.filename = 'tttt.txt'
rolnik.fields = [(60,20),(55,26)]
rolnik.farmer = "Jan"
rolnik.save()
