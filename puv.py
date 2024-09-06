class PUV:
    def __init__(self, passenger_type) -> None:
        self.passenger_type = passenger_type
        self.rate_dict = {
            'jeep' : {
                'regular' : 12.00,
                'student' : 10.00,
                'senior citizen' : 9.50
            },
            'tricycle' : {
                'regular' : 50.00,
                'student' : 40.00,
                'senior citizen' : 38.00
            },
            'bus' : {
                'regular' : 12.00,
                'student' : 10.00,
                'senior citizen' : 9.50
            }
        }
    def jeep_rate(self):
        print(f"Your fare costs ₱{self.rate_dict['jeep'][self.passenger_type]} for this jeep trip.")
    
    def tricycle_rate(self):
        print(f"Your fare costs ₱{self.rate_dict['tricycle'][self.passenger_type]} for this tricycle trip.")
    
    def bus_rate(self):
        print(f"Your fare costs ₱{self.rate_dict['bus'][self.passenger_type]} for this bus trip.")