# The volume of a sphere is (4/3)*pi*r^3. What is a volume of a sphere with radius 5?
pi = 3.14159
r = 5.0
print("The volume of a sphere with radius 5 is",(4.0/3.0)*pi*r**3)

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
# the total wholesale cost for 60 copies?
cover_price = 24.95
discount = (40/100)
base_shipping = 3.0
additional_shipping_per_unit = 0.75
order_quantity = 60

wholesale_order_cost = ((1-discount)*order_quantity*cover_price)\
                       +(base_shipping+(order_quantity-1)*additional_shipping_per_unit)
print("The total wholesale cost for",order_quantity,"books is",wholesale_order_cost)

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then
# 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get
# home for breakfast?

left_house_at = 6*60+52 #minutes since midnight
easy_pace = 60*8+15
tempo = 60*7+12
run_time = (2*easy_pace+3*tempo)/60 #runtime in minutes
arrive_home_at = left_house_at+run_time #minutes since midnight
arrive_home_hour = int(arrive_home_at/60)
arrive_home_minute = int(arrive_home_at-(60*arrive_home_hour))

print("You will arrive home at ",arrive_home_hour,":",arrive_home_minute,sep="")


