
import pickle
import json
import pandas as pd
import numpy as np



class CarPrice():
    def __init__(self, symboling, normalized_losses, fuel_type, aspiration, num_of_doors, drive_wheels,
     engine_location,wheel_base, length, width,height, curb_weight,num_of_cylinders, engine_size,bore,stroke,
     compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system):
        
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        
        self.make = "make_"+ make
        self.body_style = "body-style_" + body_style
        self.engine_type = "engine-type_" + engine_type
        self.fuel_system = "fuel-system_" + fuel_system
        


    def load_model(self):
        with open("models\LinearRegression_my_pra.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open("models\\auto_column.json", "r") as f:
            self.json_data = json.load(f)#instance variable 

    def get_car_price_prediction(self):

        self.load_model()        # Calling load_model method to get model and json_data

        make_index = self.json_data['columns'].index(self.make)
        body_style_index = self.json_data['columns'].index(self.body_style)
        engine_type_index = self.json_data['columns'].index(self.engine_type)
        fuel_system_index = self.json_data['columns'].index(self.fuel_system)

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.symboling
        array[1] = self.normalized_losses
        array[2] = self.json_data["fuel_type_values"][self.fuel_type]
        array[3] = self.json_data["aspiration_values"][self.aspiration]
        array[4] = self.json_data["num_of_doors_value"][self.num_of_doors]
        array[5] = self.json_data["drive_wheels_values"][self.drive_wheels]
        array[6] = self.json_data["engine_location_value"][self.engine_location]
        array[7] = self.wheel_base
        array[8] = self.length
        array[9] = self.width
        array[10] = self.height
        array[11] = self.curb_weight
        array[12] = self.json_data["num_of_cylinders_values"][self.num_of_cylinders]
        array[13] = self.engine_size
        array[14] = self.bore
        array[15] = self.stroke
        array[16] = self.compression_ratio
        array[17] = self.horsepower
        array[18] = self.peak_rpm
        array[19] =self.city_mpg 
        array[20] = self.highway_mpg  #21 couns we need to presict the price so we are not taking it here 
        array[make_index] = 1
        array[body_style_index] = 1
        array[engine_type_index] = 1
        array[fuel_system_index] = 1
        

        print("Test Array -->\n",array)
        predicted_price = self.model.predict([array])[0]
        print("predicted_charges",predicted_price)
        return np.around(predicted_price, 2)


if __name__ == "__main__":
    symboling = 3.00
    normalized_losses = 120.00
    fuel_type = 'diesel'
    aspiration = 'turbo'
    num_of_doors = 'two'
    drive_wheels = '4wd'
    engine_location = "front"#new
    wheel_base = 88.60
    length = 168.80
    width = 64.10
    height = 49.80
    curb_weight = 2550.00
    num_of_cylinders = "two" #new
    engine_size = 136.00
    bore = 3.47
    stroke = 2.68
    compression_ratio = 9.00
    horsepower = 120.00
    peak_rpm = 6000.00
    city_mpg = 21.00
    highway_mpg = 27.00
    #one hot encoded col
    make = "volkswagen"
    body_style = "sedan"
    engine_type = "ohc"
    fuel_system = "mpfi"
   

    object = CarPrice(symboling, normalized_losses, fuel_type, aspiration, num_of_doors, drive_wheels,engine_location,wheel_base, length, 
    width,height, curb_weight,num_of_cylinders, engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,
     make,body_style, engine_type, fuel_system)
    price = object.get_car_price_prediction()
    print()
    print(f"Predicted car price is {price}/- $. Only")