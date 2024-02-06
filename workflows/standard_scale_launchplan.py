from typing import List
from flytekit import LaunchPlan, workflow
from .standard_scale import standard_scale_workflow
from .standard_scale_with_subworkflow import generate_data

standard_scale_launch_plan = LaunchPlan.get_or_create(
    standard_scale_workflow,
    name="standard_scale_lp",
    default_inputs={"values": [3.0, 4.0, 5.0]},
)


# Embed launch plan in workflow
@workflow
def workflow_with_launchplan(num_samples: int, seed: int) -> List[float]:
    data = generate_data(num_samples=num_samples, seed=seed)
    return standard_scale_launch_plan(values=data)


if __name__ == "__main__":
    print(
        f"Running lp() {standard_scale_launch_plan(values=[float(x) for x in range(20, 30)])}"
    )
