import json

# Object to hold avocado data
# Static method to read the data set
# https://www.kaggle.com/neuromusic/avocado-prices

class Avocado:
    def __init__(self, date, avg_price, avocado_type, year, region, total_volume, plu4046, plu4225, plu4770):
        # observation date
        self.date = date
        # average price of a single avocado
        self.avg_price = avg_price
        # conventional or organic
        self.avocado_type = avocado_type
        # the year
        self.year = year
        # city or region of the observation
        self.region = region
        # total number of avocados sold
        self.total_volume_sold = total_volume
        # total number of avocados with PLU 4046 (small hass) sold
        self.plu_4046_sold = plu4046
        # total number of avocados with PLU 4225 (large hass) sold
        self.plu_4225_sold = plu4225
        # total number of avocados with PLU 4770 (extra large hass) sold
        self.plu_4770_sold = plu4770
        # labels (dictionary)
        self.extra_labels = {}

    def __str__(self):
        return json.dumps(self.__dict__)

    @staticmethod
    # parses the avocado csv data file
    async def read_data_set():
        rows = []
        file = open("data/avocado.csv")

        schema_line = True

        for line in file:
            if schema_line:
                schema_line = False
                continue

            cols = line.split(",")

            # extract required columns to create the avocado object
            rows.append(Avocado(
                cols[1],
                float(cols[2]),
                cols[11],
                int(cols[12]),
                cols[13].replace("\n", ""),
                float(cols[3]),
                float(cols[4]),
                float(cols[5]),
                float(cols[6])
            ))

        file.close()

        return rows
