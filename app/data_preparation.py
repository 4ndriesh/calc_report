from logging_err import Logger
class Data_preparation():
    def __init__(self):
        self.log = Logger()
        self.log.message_debug("Create class Data preparation")

    def tmp(self):
        Cars = {'Brand':
                ['Honda Civic',
                 'Toyota Corolla',
                 'Ford Focus',
                 'Audi A4'],

                'Price': [22000, 25000, 27000, 35000],
                'Format': [{
                    "style": {'Brand': "highlight"},
                    "merge_cell": {'Brand': [2, 0]}
                },
                    0,
                    0, {
                        "style": {'Price': "highlight"}
                    }, ]
                }
        return Cars