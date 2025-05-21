from search import perform_search

def main():
    while True:
        query = input("Enter your search query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        perform_search(query)

if __name__ == "__main__":
    main()
