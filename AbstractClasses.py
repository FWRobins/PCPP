import abc

class scanner_blueprint(abc.ABC):
    @abc.abstractmethod
    def scan_document(self, document):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass
class printer_blueprint(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MDF1(scanner_blueprint, printer_blueprint):
    def __init__(self, serial):
        self.serial = serial
        self.resolution = "800x800"

    def scan_document(self, document):
        return f"{document} has been scanned"

    def get_scanner_status(self):
        return f"resolution: {self.resolution}, serial: {self.serial}"

    def print_document(self, document):
        return f"{document} has been printed"

    def get_printer_status(self):
        return f"resolution: {self.resolution}, serial: {self.serial}"

class MDF2(scanner_blueprint, printer_blueprint):
    def __init__(self, serial):
        self.serial = serial
        self.resolution = "1080x1080"
        self.print_total = 0
        self.scan_total = 0

    def scan_document(self, document):
        self.scan_total += 1
        return f"{document} has been scanned"

    def get_scanner_status(self):
        return f"resolution: {self.resolution}, serial: {self.serial}, scan total: {self.scan_total}"

    def print_document(self, document):
        self.print_total +=1
        return f"{document} has been printed"

    def get_printer_status(self):
        return f"resolution: {self.resolution}, serial: {self.serial}, print total: {self.print_total}"

class MDF3(scanner_blueprint, printer_blueprint):
    def __init__(self, serial):
        self.serial = serial
        self.resolution = "2160x2160"
        self.print_total = 0
        self.scan_total = 0
        self.fax_total = 0

    def scan_document(self, document):
        self.scan_total += 1
        return f"{document} has been scanned"

    def get_scanner_status(self):
        return f"resolution: {self.resolution}, serial: {self.serial}, scan total: {self.scan_total}"

    def print_document(self, document):
        self.print_total +=1
        return f"{document} has been printed"

    def get_printer_status(self):
        return f"resolution: {self.resolution}, serial: {self.serial}, print total: {self.print_total}"

    def fax_document(self, document, number):
        self.fax_total +=1
        return f"{document} has been faxed to {number}"

    def get_fax_status(self):
        return f"resolution: {self.resolution}, serial: {self.serial}, fax total: {self.fax_total}"

device1 = MDF1('123456')
print(device1.scan_document('doc1'))
print(device1.get_printer_status())

device2 = MDF2('456789')
print(device2.scan_document('doc2'))
print(device2.get_scanner_status())
print(device2.print_document('doc3'))
print(device2.get_printer_status())

device3 = MDF3('789123')
print(device3.scan_document('doc4'))
print(device3.get_scanner_status())
print(device3.print_document('doc5'))
print(device3.get_printer_status())
print(device3.fax_document('doc6', '555-1023'))
print(device3.get_fax_status())
