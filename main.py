from astropy.io import ascii
import numpy as np

DATA_FILE = "data/gpw_v4_population_density_rev11_2020_2pt5_min.asc"
NO_DATA_VALUE = -9999

def get_dataframe():
	return ascii.read(DATA_FILE, format="no_header", delimiter=" ", guess=False) \
		.to_pandas() \
		.replace(NO_DATA_VALUE, 0)


def get_probabilities(df):
	# df: dataframe
	flat = np.array(df).flatten()
	probs = flat / flat.sum()
	return (flat, probs)

if __name__ == "__main__":
	data = get_dataframe()
	flat, probabilities = get_probabilities(data)

	random = np.random.choice(flat, p=probabilities)

	print(f"Random density: {random}")

