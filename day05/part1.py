filename = "input.txt"
import sys

class Range:
    def __init__(self, min, max, dest):
        self.min = min
        self.max = max
        self.dest = dest
    def __repr__(self):
        return "" + str(self.min) + "-" + str(self.max) + "..." + str(self.dest)
    

    def __str__(self):
        return "" + self.min + "-" + self.max + ", " + self.dest

def get_seeds():
    seeds = []
    with open(filename) as file:
        line = file.readline()
        lastelmnum = False
        num = ""
        for i in range(0, len(line)):
            elm = line[i]
            if elm.isnumeric():
                num += elm
                lastelmnum = True
            elif lastelmnum:
                seeds.append(int(num))
                lastelmnum = False
                num = ""
    return seeds

def get_map(starter):
    seed_to_soil = []
    file_len = 0
    start = 0
    with open(filename) as file:
        lines = file.readlines()
    with open(filename) as file:
        file_len = len(file.readlines())
    with open(filename) as file:
        line_num = 0
        for line in file:
            word = ""
            for i in range(0, len(line)):
                elm = line[i]
                word += elm
                if (word == starter):
                    start = line_num+1
                    break
                elif (len(word) > 12):
                    break
            line_num += 1
    
    end = False
    for i in range(start, file_len):
        if end: break
        line = lines[i]
        nums = []
        lastelmnum = False
        num = ""
        for j in range(0, len(line)):
            elm = line[j]
            if j == 0 and not elm.isnumeric():
                end = True
                break
            else:
                if elm.isnumeric():
                    num += elm
                    lastelmnum = True
                elif lastelmnum:
                    nums.append(int(num))
                    lastelmnum = False
                    num = ""
                    if len(nums) == 3:
                        source = nums[1]
                        dest = nums[0]

                        ranger = nums[2]
                        seed_to_soil.append(Range(source, source+ranger-1, dest))
                        # for i in range(0, nums[2]):
                        #     seed_to_soil[source+i] = dest+i                   
    return seed_to_soil

seeds = get_seeds()
seed_to_soil = get_map("seed-")
soil_to_fertilizer = get_map("soil-")
fertilizer_to_water = get_map("fertilizer-")
water_to_light = get_map("water-")
light_to_temp = get_map("light-")
temp_to_humidity = get_map("temperature-")
humidity_to_location = get_map("humidity-")

def print_maps():
    print(seeds)
    print(seed_to_soil)
    print(soil_to_fertilizer)
    print(fertilizer_to_water)
    print(water_to_light)
    print(light_to_temp)
    print(temp_to_humidity)
    print(humidity_to_location)

def get_mapping(key, list):
    value = key
    for range in list:
        if key >= range.min and key <= range.max:
            diff = key - range.min
            value = range.dest + diff
    return value

def get_location(seed):
    soil = get_mapping(seed, seed_to_soil)
    fertilizer = get_mapping(soil, soil_to_fertilizer)
    water = get_mapping(fertilizer, fertilizer_to_water)
    light = get_mapping(water, water_to_light)
    temp = get_mapping(light, light_to_temp)
    humidity = get_mapping(temp, temp_to_humidity)
    location = get_mapping(humidity, humidity_to_location)
    # soil = seed_to_soil[seed] if seed in seed_to_soil.keys() else seed
    # fertilizer = soil_to_fertilizer[soil] if soil in soil_to_fertilizer.keys() else soil
    # water = fertilizer_to_water[fertilizer] if fertilizer in fertilizer_to_water.keys() else fertilizer
    # light = water_to_light[water] if water in water_to_light.keys() else water
    # temp = light_to_temp[light] if light in light_to_temp.keys() else light
    # humidity = temp_to_humidity[temp] if temp in temp_to_humidity.keys() else temp
    # location = humidity_to_location[humidity] if humidity in humidity_to_location.keys() else humidity
    return location

min_location = sys.maxsize

for seed in seeds:
    location = get_location(seed)
    min_location = location if location < min_location else min_location
print(min_location)




