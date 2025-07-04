import requests
import json

def main():
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # GET
    print("=== GET Example ===")
    response = requests.get(f"{BASE_URL}/posts/1")
    print(f"Status: {response.status_code}")
    print(f"Data: {response.json()}")
    
    # POST
    print("\n=== POST Example ===")
    data = {"title": "Nuevo post", "body": "Contenido", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    print(f"Status: {response.status_code}")
    print(f"Created: {response.json()}")
    
    # PUT
    print("\n=== PUT Example ===")
    data = {"id": 1, "title": "Post actualizado", "body": "Nuevo contenido", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=data)
    print(f"Status: {response.status_code}")
    print(f"Updated: {response.json()}")
    
    # DELETE
    print("\n=== DELETE Example ===")
    response = requests.delete(f"{BASE_URL}/posts/1")
    print(f"Status: {response.status_code}")
    print("Deleted successfully" if response.status_code == 200 else "Delete failed")

if __name__ == "__main__":
    main()