import test_c
import maps

# GetDirection
#     - This method will be used to find the angle that device should direct to
#     - The purpose of this method is to lead the device to actual direction
# 
# Params
#     origin            : string
#         - User or Device Position on Maps. The value are longitude and latitude of the user position.
#         - The format will be "longitude,latitude"
#         - Example : "-6.123456,106.123456"
# 
#     destination       : string
#         - In here drivingPosition will be used to get the nearest point from the path.
#         - This path means the correct direction to goal
#         - The format will be "longitude,latitude"
#         - Example : "-6.123456,106.123456"
# 
#     mode              : string
#         - Contains : "driving", "walking", "bicycling", "transit"
#         - DeviceAngle is used to get the actual direction of the device (smartphone)
#         - This value is used to find the angle that should direct to
#         - The value is in range [-360 360]
#         - Example : "45"
# 
# Return
#     angle    : string
#         - The device angle that should direct to
# 
def GetDirection(origin, destination, mode):
	res = {}
	res["direction"] = maps.get_direction(origin, destination, mode)
	return res

def Test(name):
	f = test_c.Foo()

	res = {}
	res["res"] = f.sayname(name)
	return res


def GetStep(origin, destination, angle):
	gmaps = maps.Maps()
	res = {}
	res["res"] = gmaps.get_direction()
	return res