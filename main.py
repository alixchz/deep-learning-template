import torch
import torch.nn as nn

if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print('Using {} device'.format(device))