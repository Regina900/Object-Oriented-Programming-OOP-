class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        return f"Calling {number} from {self.model}..."

    def charge(self):
        return f"{self.model} is charging. Battery: {self.battery}%"

class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a {self.camera_megapixels}MP photo with {self.model}!"

# Example usage:
phone1 = Smartphone("Samsung", "Galaxy S22", "128GB", 85)
print(phone1.call("123-456-7890"))
print(phone1.charge())

phone2 = SmartphonePro("Apple", "iPhone 15 Pro", "256GB", 90, 48)
print(phone2.take_photo())
