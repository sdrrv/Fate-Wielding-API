class model:
    def __init__(self):
        self.db = {
            "images":{
                "coin":{
                    "Head": "https://www.random.org/coins/faces/60-usd/0100c-washington/obverse.jpg",
                    "Tail": "https://www.random.org/coins/faces/60-usd/0100c-washington/reverse.jpg"
                },
                "dice":"https://www.random.org/dice/dice"
            }
        }
    
    def get_images(self):
        return self.db["images"]

    def get_coin_image(self, coinFace):
        return self.db["images"]["coin"][coinFace]
    
    def get_dice_image(self, diceRoll):
        return self.db["images"]["dice"] + str(diceRoll) + ".png"