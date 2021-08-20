from models.model import model

class tools:
    def __init__(self):
        self.model = model() 

    def parse_string_list(self, lister):
        return lister[1:-1].split(",")

    def get_coin_image(self, coinFace):
        return self.model.get_coin_image(coinFace)

    def get_response(self,response):
        return {
        "response": response,
        "type": str(type(response))
    }


    def get_response_image(self, response, imageURL):
        return {
            "response": response,
            "image": imageURL,
            "type": str(type(response))
        }