# connect to rockset and list all collections
from rockset import Client
rs = Client(api_server='api.rs2.usw2.rockset.com',
            api_key='4UXp24ceoewlfu59reP0icx49HH9IvDfDSYx6vsOCCa1hXS3NVJYFdRk9BhKaqgn')
print([vars(c) for c in rs.Collection.list()])