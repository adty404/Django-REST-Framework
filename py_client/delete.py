import requests

product_id = input("Enter the product id: ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"Invalid id: {product_id}")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint) # HTTP Request
    print(get_response.status_code, get_response.status_code==204)