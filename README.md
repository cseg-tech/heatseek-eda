# heatseek-eda
Exploratory Data Analysis for Heat Seek

## Notes

* Please keep all data in the `/data/` directory. The repository is set up to ignore everything in this directory.
* If you add any scripts, please add usage documentation to the appropriate section in the README.
* Please keep EDA results outside of this repository. If using a jupyter notebook, please clear your outputs before committing. If generating plots or graphcs, please generate them into the `/data/` repository.
* On your first commit to the repository, add yourself to the list of contributors!

## Scripts

### scrub.py
* `Usage: python scrub.py raw_input clean_output`
* Removes potentially identifiable information from the directly exported dataset for analysis.

### per_user.py
* `Usage: python per_user.py dataset output_dir/`
* Separates aggregate data into datasets for individual users.
* Also includes `user_import(filepath)`, a function for importing the dataset per-user.
* `from per_user import user_import`

## Contributors
* Jake Lee, @jakehlee
* Daniel Jaroslawicz, @djaroslawicz
* Justin Won, @1jinwoo
