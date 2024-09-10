from tabulate import tabulate
class PUV:
    def __init__(self, vehicle_type) -> None:
        self.vehicle_type = vehicle_type
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
        self.header = ["Passenger\nType", f"{self.vehicle_type.title()} Fare\n(₱)"]
        self.rows = [[key.title(),f"₱ {value:.2f}"] for key,value in self.rate_dict[self.vehicle_type].items()]
        print(tabulate(self.rows, headers= self.header,tablefmt= "fancy_grid", colalign= ("center", "center")))
    def fare_rate(self, passenger_type):
        return f"Your fare costs ₱{self.rate_dict[self.vehicle_type][passenger_type]:.2f} for this {self.vehicle_type} trip."