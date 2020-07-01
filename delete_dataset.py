# Delete a Dataset in Bigquery

from google.cloud import bigquery
import argparse


def delete_dataset(datasetid):

    """ Deletes an already present dataset in BigQuery by passing
        the dataset ID as parameter in the command line."""

    try:
        client = bigquery.Client()
        dataset_id = "{}.{}".format(client.project,datasetid)
        client.delete_dataset(dataset_id,delete_contents=True,not_found_ok=True)
        return True
    except Exception as e:
        print(e.args)
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("datasetid",help="Unique Name of dataset id")
    args = parser.parse_args()
    if delete_dataset(args.datasetid):
        print("Dataset with name: {} is successfully deleted.".format(args.datasetid))
