import time
from typing import Tuple

import tqdm
import torch
import numpy as np


def count_parameters(model) -> int:
    pytorch_total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return pytorch_total_params


def get_inference_durations_on_rand_frontend(
    model,
    samples_count: int = 1000,
    input_shape: Tuple = (1, 1, 80, 404),
    device: str = "cpu",
) -> np.ndarray:
    durations = []
    for _ in tqdm.tqdm(range(samples_count)):
        random_input = torch.rand(input_shape, device=device)
        start = time.time()
        model(random_input)
        end = time.time()
        durations.append(end - start)
    return np.array(durations)
