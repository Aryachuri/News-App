import requests

def fetch(query, lan, category):
    url = "https://newsdata.io/api/1/latest"

    params = {
        "apikey": "pub_8a944f6f3eaa4d96bcadf83aabee194d",
        "language": lan,
        "removeduplicate": "1",
    }

    if category:
        params["category"] = category

    if query:
        params["q"] = query

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        print(data)
        return

    if not data.get("results"):
        print("No news found.")
        return

    for i, news in enumerate(data["results"], start=1):
        print(f"\nNews {i}")
        print(f"Title: {news['title']}")
        print(f"Description: {news['description']}")
        print("-" * 60)
         


def language():
                print("1.English")
                print("2.Hindi")
                print("3.Russian")
                print("4.Korean")

                language=int(input("Enter the language in which you want to read the news: "))

                if(language==1):
                    return 'en'
                elif(language==2):
                    return 'hi'
                elif(language==3):
                    return 'ru'
                elif(language==4):
                    return 'ko'

while True:
    print("1.To Read Bussiness related news ")
    print("2.To Read Sports related news")
    print("3.To Read Politics related news")
    print("4.To Read Food related news")
    print("5.To Read Lifestyle related news")
    print("6.To Read Crime related news")
    print("7.To Read Breaking news")
    print("8.To Read Domestic news")
    print("9.To Read Education related news")
    print("10.To Read Enviornment related news")
    print("11.Exit")


    choice=int(input("Enter the option for which you want to read the news: "))
    match(choice):
        case 1:
            query="Business"
            lan=language()
            category="business"
            fetch(query,lan,category)
            
        case 2:
            query="Sports"
            lan=language()
            category="sports"
            fetch(query,lan,category)
        
        case 3:
            query="Politics"
            lan=language()
            category="politics"
            fetch(query,lan,category)
            
        case 4:
            query="Food"
            lan=language()
            category="food"
            fetch(query,lan,category)
            
        case 5:
            query="Lifestyle"
            lan=language()
            category="lifestyle"
            fetch(query,lan,category)
            
        case 6:
            query="Crime"
            lan=language()
            category="crime"
            fetch(query,lan,category)
            
        case 7:
            query="Breaking"
            lan=language()
            category="breaking"
            fetch(query,lan,category)
            
        case 8:
            query="Domestic"
            lan=language()
            category="domestic"
            fetch(query,lan,category)
            
        case 9:
            query="Education"
            lan=language()
            category="education"
            fetch(query,lan,category)
            
        case 10:
            query="Environment"
            lan=language()
            category="environment"
            fetch(query,lan,category)
            
        case 11:
            print("Exiting ...")
            break
        case _:
            print("Invalid choice!")
        
              
            
                






