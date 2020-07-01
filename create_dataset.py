# Create a Dataset in Bigquery

from google.cloud import bigquery
import argparse


def create_dataset(datasetid):

    """ Creates a dataset in BigQuery by passing
        the unique dataset ID as parameter in the
        command line."""

    try:
        client = bigquery.Client()
        dataset_id = "{}.{}".format(client.project,datasetid)
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        dataset = client.create_dataset(dataset)
        return True
    except Exception as e:
        print(e.args)
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("datasetid",help="Unique Name of dataset id")
    args = parser.parse_args()
    if create_dataset(args.datasetid):
        print("Dataset with name: {} is successfully created.".format(args.datasetid))
