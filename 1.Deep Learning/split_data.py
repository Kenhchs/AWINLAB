import splitfolders

input_folder = './flowers'

# Split with ratio
# In my case, 0.7 for train, 0.2 for validation, 0.1 for test
splitfolders.ratio(input_folder, output="dataset", seed=42, ratio=(.7, .2, .1), group_prefix=None)