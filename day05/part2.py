filename = "example.txt"
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
    def __lt__(self, other):
        return self.min < other.min
    

def get_seeds():
    seeds = set()
    current_seeds = []
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
                current_seeds.append(int(num))
                lastelmnum = False
                num = ""
                if len(current_seeds) == 2:
                    start = current_seeds[0]
                    ranger = current_seeds[1]
                    for i in range(0, ranger):
                        seeds.add(start+i)
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
    return seed_to_soil

seeds = get_seeds()
print("got seeds")
seed_to_soil = get_map("seed-")
soil_to_fertilizer = get_map("soil-")
fertilizer_to_water = get_map("fertilizer-")
water_to_light = get_map("water-")
light_to_temp = get_map("light-")
temp_to_humidity = get_map("temperature-")
humidity_to_location = get_map("humidity-")
print("got all maps")

def sort_maps():
    seed_to_soil.sort()
    soil_to_fertilizer.sort()
    fertilizer_to_water.sort()
    water_to_light.sort()
    light_to_temp.sort()
    temp_to_humidity.sort()
    humidity_to_location.sort()
def print_maps():
    print(seeds)
    print(seed_to_soil)
    print(soil_to_fertilizer)
    print(fertilizer_to_water)
    print(water_to_light)
    print(light_to_temp)
    print(temp_to_humidity)
    print(humidity_to_location)
def remove_all_but_one(list):
    while len(list) > 1:
        list.pop()
def make_lists_len_one():
    remove_all_but_one(seed_to_soil)
    remove_all_but_one(soil_to_fertilizer)
    remove_all_but_one(fertilizer_to_water)
    remove_all_but_one(water_to_light)
    remove_all_but_one(light_to_temp)
    remove_all_but_one(temp_to_humidity)
    remove_all_but_one(humidity_to_location)

sort_maps()
print("maps sorted")
# make_lists_len_one()
# print("lists len one")
print_maps()


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid].min <= x and arr[mid].max >= x:
            diff = x - arr[mid].min
            return arr[mid].dest + diff
        # If element is greater than mid.min, then it can only
        # be present in right subarray
        elif arr[mid].min > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in left subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return x


def get_mapping(key, list):
    # return binary_search(list, 0, len(list)-1, key)
    value = key
    

def get_location(seed):
    soil = get_mapping(seed, seed_to_soil)
    fertilizer = get_mapping(soil, soil_to_fertilizer)
    water = get_mapping(fertilizer, fertilizer_to_water)
    light = get_mapping(water, water_to_light)
    temp = get_mapping(light, light_to_temp)
    humidity = get_mapping(temp, temp_to_humidity)
    location = get_mapping(humidity, humidity_to_location)
    return location

min_location = sys.maxsize
cur = 0.0
i = 0
for seed in seeds:
    location = get_location(seed)
    min_location = location if location < min_location else min_location
    i += 1
    percentage = i / len(seeds)
    if percentage - cur  >= 0.01:
        cur = percentage
        # print("{:.0f}".for
        # 
        # mat( cur*100 ) + "%") 

print(min_location)





