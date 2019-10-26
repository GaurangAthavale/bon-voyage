airports = ['Ahmedabad','Amritsar','Bengaluru','Chennai','Cochin','Goa','Guwahati','Hyderabad','Kolkata','Mumbai','Delhi','Thiruvananthapuram','Port Blair','Nagpur','Jaipur','Lucknow','Varanasi','Mangalore','Coimbatore','Imphal','Vijayawada']
ap_codes = ['AMD', 'ATQ', 'BLR', 'MAA', 'COK', 'GOI', 'GAU', 'HYD', 'CCU', 'BOM', 'DEL', 'TRV', 'IXZ', 'NAG', 'JAI', 'LKO', 'VNS', 'IXE', 'CJB', 'IMF', 'VGA']

ap_converter = dict()
for i in range(len(airports)):
    ap_converter[ap_codes[i]] = airports[i]

print(ap_converter)