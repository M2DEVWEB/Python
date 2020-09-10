from requests import get

def retrieve(department_param):
  req = get('https://lefooding.com/fr/search?type=restaurant&page=1&sort=&per_page=20&total_pages=1')
  results = req.json()['results']

  data_return = []

  for data in results:
    name = data['name']
    address = data['address']
    department = address['department']
    position = address['position']
    long = position[0]
    lat = position[1]
    price = data['price'][0]
    db_object = {'name':name, 'long':long, 'lat':lat, 'price': price}
    if department_param in department:
      data_return.append(db_object)

  return data_return
