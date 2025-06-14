from keras.utils import split_dataset
from torch.utils.data import Dataset
def load(dir: str):
    dataset = split_dataset(path=dir, split="train")
    dataset[0]["image"]