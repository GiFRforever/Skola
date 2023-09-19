from tpblite import TPB

def search_pirate_bay(query):
    tpb = TPB()
    results = tpb.search(query)
    
    for i, result in enumerate(results):
        print(f"Result {i + 1}:")
        print(f"Title: {result['name']}")
        print(f"Seeders: {result['seeders']}")
        print(f"Leechers: {result['leechers']}")
        print(f"Magnet link: {result['magnet_link']}")
        print("--------------------------")
        
# Example usage
search_pirate_bay("Game of Thrones")
