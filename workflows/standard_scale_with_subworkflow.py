import random
from typing import List
from flytekit import task, workflow

from .standard_scale import standard_scale_workflow
from .hello_world import say_hello

@task
def generate_data(num_samples: int, seed: int) -> List[float]:
    random.seed(seed)
    return [random.random() for _ in range(num_samples)]


@workflow
def workflow_with_subworkflow(num_samples: int, seed: int = 3) -> List[float]:
    say_hello_task = say_hello(name="StandardScaleWorkflow")
    data = generate_data(num_samples=num_samples, seed=seed)

    # specify dependency
    say_hello_task >> data
    return standard_scale_workflow(values=data)
