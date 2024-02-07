import math
from typing import List

from flytekit import map_task, task, workflow


@task
def sum_and_length(data: List[float]) -> List[float]:
    """Return the sum and length of a dataset of numbers."""
    return [sum(data), float(len(data))]


@task
def prepare_partitions(data: List[float], n_partitions: int) -> List[List[float]]:
    """Create partitions from the full dataset."""
    size = math.ceil(len(data) / n_partitions)
    return [data[size * i : size * (i + 1)] for i in range(n_partitions)]


@task
def reduce(results: List[List[float]]) -> float:
    """Combine results from the map task."""
    total, length = 0.0, 0.0
    for sub_total, sub_length in results:
        total += sub_total
        length += sub_length
    return total / length


@task
def generate_compute_mean_data(num_samples: int) -> List[float]:
    return [float(x) for x in range(num_samples)]


@workflow
def parallelized_compute_mean(num_samples: int, n_partitions: int = 10) -> float:
    """An embarrassingly parallel implementation to compute the mean from data."""
    data = generate_compute_mean_data(num_samples=num_samples)
    partitioned_data = prepare_partitions(data=data, n_partitions=n_partitions)

    # use map_task to apply the sum_and_length task to the partitions
    results = map_task(sum_and_length)(data=partitioned_data)

    return reduce(results=results)
