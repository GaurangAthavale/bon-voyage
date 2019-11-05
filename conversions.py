airports = ['Ahmedabad','Bengaluru','Chennai','Goa','Hyderabad','Kolkata','Mumbai','Delhi','Port Blair','Jaipur','Varanasi','Mangalore','Coimbatore']
ap_codes = ['AMD', 'BLR', 'MAA', 'GOI', 'HYD', 'CCU', 'BOM', 'DEL', 'IXZ', 'JAI', 'VNS', 'IXE', 'CJB']

ap_converter = dict()
for i in range(len(airports)):
    ap_converter[ap_codes[i]] = airports[i]

def find_flt_duration(dep, arr, dd, ad):
    dep_hr, dep_min = list(map(int, dep.split(':')))
    arr_hr, arr_min = list(map(int, arr.split(':')))
    # print(dep_hr, arr_hr, dep_min, arr_min)
    # print(dd, ad)
    if ad > dd:
        arr_hr += 24
    hrs = arr_hr - dep_hr
    mins = arr_min - dep_min
    if mins < 0:
        hrs -= 1
        mins += 60
    return '{:02d}'.format(hrs) + ':' + '{:02d}'.format(mins)

def find_dur_mins(dur):
    hrs, mins = dur.split(':')
    ans = int(mins) + int(hrs)*60
    return ans

def find_dur_mins_tr(dur):
    hrs, mins = dur.split(':')
    hrs = hrs.strip()[:-1]
    mins = mins.strip()[:-1]
    # print(hrs, mins)
    ans = int(mins) + int(hrs)*60
    return ans

# print(find_dur_mins_tr('26H :2M'))