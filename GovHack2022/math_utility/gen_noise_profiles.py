import random
import numpy as np

from . import PERIOD


def generate_noise_profiles(n: int):
    print(f"Generating {n} noise profiles. This will take a minute...")
    return
    noise_profiles: list = []
    for i in range(0, n):
        n_noise_aggregates = 300
        all_noise_aggregates = []
        for j in range(0, n_noise_aggregates):
            random_offset = 2 * np.pi * random.random()
            random_frequency = random.randrange(0.01 * n_noise_aggregates, n_noise_aggregates)
            noise_aggregate = [
                (2 * np.pi) * (x/PERIOD + random_offset) * random_frequency
                for x in range(0, PERIOD, 1)
            ]
            all_noise_aggregates.append(
                (np.sin(noise_aggregate) + 1)
                * ((1 * random.random()) / n_noise_aggregates)
                * (1/(random.random() * random_frequency))
            )
        noise_aggregate_sum = all_noise_aggregates[0]
        for j in range(1, n_noise_aggregates):
            noise_aggregate_sum += all_noise_aggregates[j]
        noise_profiles.append(noise_aggregate_sum)
    print("Done")
    return noise_profiles
