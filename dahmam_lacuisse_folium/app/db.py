from json import load

def get(json):
  db_data = {}
  with open(json) as json_file:
    db_data = load(json_file)

  data_return = []

  for data in db_data:
    name = data['name']
    address = data['address']
    long = address[4][0]
    lat = address[4][1]
    db_object = {'name':name, 'long':long, 'lat':lat}
    data_return.append(db_object)

  return data_return
