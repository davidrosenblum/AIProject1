import asyncio
import json
from Avocado import Avocado

# builds the organization model
def build_model(data_set):
    model = {}

    for row in data_set:
        # create year if it does not exist
        if row.year not in model:
            model[row.year] = {}

        # create region if it does not exist in the year
        if row.region not in model[row.year]:
            model[row.year][row.region] = {}

        # create avocado type if it does not exist in the year's region
        # initialize with 0 for numerical values that are updated later
        if row.avocado_type not in model[row.year][row.region]:
            model[row.year][row.region][row.avocado_type] = {
                'total': 0, '4046': 0, '4225': 0, '4770': 0, 'avg_price': 0, "count": 0
            }

        # update volume, price, frequency data
        model[row.year][row.region][row.avocado_type]["total"] += round(row.total_volume_sold)
        model[row.year][row.region][row.avocado_type]["4046"] += round(row.plu_4046_sold)
        model[row.year][row.region][row.avocado_type]["4225"] += round(row.plu_4225_sold)
        model[row.year][row.region][row.avocado_type]["4770"] += round(row.plu_4770_sold)
        model[row.year][row.region][row.avocado_type]["avg_price"] += row.avg_price
        model[row.year][row.region][row.avocado_type]["count"] += 1

    # for each group... calculate averages
    for year in model:
        for region in model[year]:
            for a_type in model[year][region]:
                group = model[year][region][a_type]
                group["avg_price"] = round(group["avg_price"] / group["count"], 2)

    return model


# main method
# loads the data (async) and creates the model
async def main():
    # load the data set
    data_set = await Avocado.read_data_set()

    # construct the model with the data set
    model = build_model(data_set)

    # print the model
    print(json.dumps(model, indent="\t"))


# call main
if __name__ == "__main__":
    asyncio.run(main())
