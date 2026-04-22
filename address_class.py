class Address:
    def __init__(self, zip_code, city):
        self.zip_code = zip_code
        self.city = city

    def address_info(self):
        return {
            "zip_code": self.zip_code,
            "city": self.city
        }