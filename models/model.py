class model:
    def __init__(self):
        self.db = {
            "images":{
                "coin":{
                    "Heads": "https://www.random.org/coins/faces/60-usd/0100c-washington/obverse.jpg",
                    "Tail": "https://www.random.org/coins/faces/60-usd/0100c-washington/reverse.jpg"
                }
            }
        }
    
    def get_images(self):
        return self.db["images"]