
class Json_processor:

    def get_value_from_json(self, name, data_json):
        
        #Recuperar dades del json
        return [entry[name] for entry in data_json['indicator']['values']]