import pandas as pd
# from categories import *
import re


# Read data from CSV file, sort, and create a pickle file
# To be run only once as data sorting could take time
# Running to be handled in main()
def read_data_from_csv():
    revised_df = pd.DataFrame()
    products = pd.read_csv(DATA_FILE)
    # products = products.set_index('product_name')
    for index, row in products.iterrows():
        for category in category_dict:
            if category in row['product_name']:
                if len(revised_df) == 0:
                    revised_df = row.to_frame()
                else:
                    revised_df = revised_df.join(row.to_frame(),lsuffix='Union')
                    pass

    # print revised_df.head()
    revised_df.to_pickle(PICKLE_FILE)


# Read data from pickle file
def read_data_from_pickle():
    # print data
    return pd.read_pickle(PICKLE_FILE)


def clean_data(data):
    data.iloc[1:, 2:] = data.iloc[1:, 2:].applymap(lambda v: '' if clear_bad_data(v) else v)
    data = data.fillna('')
    return data.T


def clear_bad_data(cell):
    # print cell
    regexp = re.compile(r'(\d*\.?\d-\d*\.?\d*)+')
    if regexp.search(cell):
        return True
    return False


def cleaned_data_to_csv(cleaned_data):
    cleaned_data.to_csv(OUTPUT_FILE, sep=',')


# Main method
if __name__ == '__main__':
    print ("Starting Application")

    read_data_from_csv()
    data = read_data_from_pickle()
    # print data
    data = data.fillna('')
    cleaned_data = clean_data(data)
    cleaned_data_to_csv(cleaned_data)

    print "Run Successful!"