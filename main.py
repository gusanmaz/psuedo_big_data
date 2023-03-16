from graph import train_routes, train_routes_visualiser
from graph import social_media, social_media_visualiser
import tabular.bank as bank
import tabular.student as education
import tabular.file_path as fpath
import tabular.earthquake as quake
import os


def csv_to_md(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            csv_path = os.path.join(directory, filename)
            md_path = os.path.join(directory, filename.replace('.csv', '.md'))
            os.system(f"csvtomd {csv_path} > {md_path}")


def main():
    bank.generate()
    education.generate()
    fpath.generate()
    quake.generate()

    train_routes.generate()
    train_routes_visualiser.visualize()

    social_media.generate()
    social_media_visualiser.visualize()

    # You don't need to uncomment unless you want md version of CSV files.
    #csv_to_md("data/graph/")
    #csv_to_md("data/tabular/")


if __name__ == "__main__":
    main()




