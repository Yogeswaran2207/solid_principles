class Printer:
    def print_document(self, document):
        print(f"Printing document: {document}")


class Scanner:
    def scan_document(self):
        return "Scanned document"


class MultiFunctionDevice(Printer, Scanner):
    def print_and_scan(self, document):
        self.print_document(document)
        return self.scan_document()


# Usage
mfd = MultiFunctionDevice()
mfd.print_and_scan("My Document")