from math import sqrt
from flytekit import workflow, task
from typing import List


@task
def mean(values: List[float]) -> float:
    return sum(values) / len(values)


@task
def standard_deviation(values: List[float], mu: float) -> float:
    variance = sum([(x - mu) ** 2 for x in values])
    return sqrt(variance)


@task
def standard_scale(values: List[float], mu: float, sigma: float) -> List[float]:
    return [(x - mu) / sigma for x in values]


@task
def buggy_standard_scale(values: List[float], mu: float, sigma: float) -> float:
    """
    🐞 The implementation and output type of this task is incorrect! It should
    be List[float] instead of a sum of all the scaled values.
    """
    return sum([(x - mu) / sigma for x in values])


@workflow
def standard_scale_workflow(values: List[float]) -> List[float]:
    mu = mean(values=values)
    sigma = standard_deviation(values=values, mu=mu)
    return standard_scale(values=values, mu=mu, sigma=sigma)


if __name__ == "__main__":
    # Execute the workflow by invoking it like a function and passing in
    # the necessary parameters
    print(
        f"Running wf() {standard_scale_workflow(values=[float(i) for i in range(1, 11)])}"
    )
