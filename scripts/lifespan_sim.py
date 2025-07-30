import enum
from dataclasses import dataclass

import pandas as pd
import plotnine as plt9


def months_to_duration(total_months: int) -> str:
    num_years, num_months = divmod(total_months, 12)

    return f"{int(num_years)} years, {int(num_months)} months"


def months_to_duration_short(total_months: int) -> str:
    num_years, num_months = divmod(total_months, 12)

    return f"{int(num_years)}y {int(num_months)}m"


def months_to_years_duration(total_months: int) -> str:
    num_years, _ = divmod(total_months, 12)

    return f"{int(num_years)} years"


def create_years_months_labels(values: list[int]) -> list[str]:
    return [str(int(v / 12)) for v in values]


class TrainingStrategy(enum.Enum):
    TrainAndRest = enum.auto()
    OnlyRest = enum.auto()
    OnlyDrills = enum.auto()
    OnlyErrantry = enum.auto()


class Food(enum.Enum):
    Tofu = enum.auto()
    AnythingElse = enum.auto()


@dataclass(frozen=True)
class Case:
    lifespan: int
    training: TrainingStrategy
    food: Food


def main() -> None:
    cases = [
        Case(
            lifespan=lifespan,
            training=training,
            food=food,
        )
        for lifespan in [1500, 2500]
        # for lifespan in [1350, 2625]
        for training in [
            TrainingStrategy.TrainAndRest,
            TrainingStrategy.OnlyRest,
            TrainingStrategy.OnlyDrills,
            TrainingStrategy.OnlyErrantry,
        ]
        for food in [Food.AnythingElse, Food.Tofu]
    ]

    data = []
    for case in cases:
        print(case)

        lifespan = case.lifespan
        num_months = 0

        data.append(
            {
                "case": case,
                "training": case.training.name,
                "food": case.food.name,
                "starting_lifespan": case.lifespan,
                "lifespan": lifespan,
                "num_months": num_months,
            }
        )

        while lifespan > 0:
            # Each month
            if case.training == TrainingStrategy.OnlyDrills:
                lifespan -= 28  # drill at ~300 to 499 stress and fatigue
            elif case.training == TrainingStrategy.OnlyErrantry:
                lifespan -= 20  # errantry at 0 stress and fatigue
            elif case.training == TrainingStrategy.TrainAndRest:
                lifespan -= 44  # Assumes one instance of -2 stress and -2 fatigue lifespan penalty
            else:
                lifespan -= 40  # no loss due to stress and fatigue

            if lifespan < 0:
                lifespan = 0

            if lifespan > 0:
                if case.food == Food.Tofu:
                    lifespan += 5

            num_months += 1

            data.append(
                {
                    "case": case,
                    "training": case.training.name,
                    "food": case.food.name,
                    "starting_lifespan": case.lifespan,
                    "lifespan": lifespan,
                    "num_months": num_months,
                }
            )

        print("\t" + months_to_duration(num_months))

    data = pd.DataFrame(data)
    print(data)

    data_2 = pd.DataFrame(
        [
            {
                "case": str(case),
                "training": case.training.name,
                "food": case.food.name,
                "starting_lifespan": case.lifespan,
                "age": data[data["case"] == case]["num_months"].max(),
            }
            for case in data["case"].unique()
        ]
    )

    data_2["training"] = pd.Categorical(
        data_2["training"],
        categories=[s.name for s in sorted(TrainingStrategy, key=lambda s: s.value)],
    )

    data_2["age_years"] = [months_to_duration_short(m) for m in data_2["age"]]

    """
    plot = (
        plt9.ggplot(data, plt9.aes("num_months", "lifespan", color="training"))
        + plt9.facet_grid("food", "starting_lifespan")
        + plt9.geom_line()
        + plt9.geom_point(data=data[data["lifespan"] == 0])
        + plt9.scale_x_continuous(
            labels=create_years_months_labels, breaks=[y * 12 for y in range(0, 16, 2)]
        )
        + plt9.xlab("Years")
        + plt9.ylab("Lifespan")
    )
    """

    plot = (
        plt9.ggplot(data_2, plt9.aes("training", "age"))
        + plt9.facet_grid("food", "starting_lifespan")
        + plt9.geom_col()
        + plt9.geom_text(
            plt9.aes(label="age_years"),
            size=8,
            va="bottom",
            nudge_y=1,
        )
        + plt9.scale_y_continuous(
            labels=create_years_months_labels, breaks=[y * 12 for y in range(0, 16, 2)]
        )
    )

    plot.save("lifespan_sim.png", dpi=300)


if __name__ == "__main__":
    main()
