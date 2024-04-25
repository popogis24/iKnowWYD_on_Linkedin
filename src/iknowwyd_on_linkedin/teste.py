import requests

class GetModelResults:
    def __init__(self, texts: list):
        self.texts = texts
        self.url = 'https://radar-app.vizhub.ai/api/checkTexts'

    def get_results(self):
        model_results = {}
        for i in range(0,4):
            payload = {
                        "texts":self.texts,
                        "model_index":i
                        }
            r = requests.post(self.url, json=payload)
            result = r.json().get('results')[0].get('p')
            model_results[f"model {i}"] = result
            i = i + 1
        return model_results
    
if __name__ == "__main__":
    texts = ["I am a software engineer"]
    model_results = GetModelResults(texts).get_results()
    for i in model_results:
        print(f"{i} : {model_results[i]}")