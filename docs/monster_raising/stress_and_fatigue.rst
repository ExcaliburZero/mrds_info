
.. _stress:

.. _fatigue:

Stress & fatigue
================
Each monster has stress and fatigue score that impact various things such as their :ref:`lifespan <lifespan>`.

Things that change them
-----------------------
There are several different types of things that can increase or decrease a monster's stress or fatigue.

Both stress and fatigue are limited to the range :code:`0` to :code:`999`. If an increase would cause one to go above :code:`999`, then it only increases to :code:`999`. If a decrease would cause one to go below :code:`0`, then it only decreases to :code:`0`.

Resting
^^^^^^^
Resting decreases your current monster's stress and fatigue.
-139?? -359
       -356
-359   -350

TODO

End of a month
^^^^^^^^^^^^^^
TODO

Tournaments
^^^^^^^^^^^
Participating in a tournament decreases that monster's stress but increases their fatigue.

Items
^^^^^
There are several :ref:`items <items>` that impact stress and fatigue. These are broken down into three categories:

* Consumable items
* Passive items
* Monthly food

Consumable
""""""""""

.. csv-table::
    :header: Name, Stress impact, Price

    Monster Candy, -30, 100 G
    Elixir, -100, 250 G
    Sea Angel, -200, 400 G
    Blade Weed, +100, 200 G

.. csv-table::
    :header: Name, Fatigue impact, Price

    Banana Ring, -30, 100 G
    Medicinal Herb, -100, 250 G
    Honey Shroom, -300, 500 G
    Fatty Meat, +50, 100 G

Passive
"""""""

.. csv-table::
    :header: Name, Season, Trigger, Stress decrease, Fatigue decrease

    Sculpture, All, Monthly, , ???
    Gemini's Pot, All, Monthly, ???,
    Weather Doll, Spring, Monthly, , ???
    Ice Cube, Summer, Monthly, ???,
    Cricket Chime, Autumn, Monthly, ???,
    Fire Stone, Winter, Monthly, , ???
    Music Box, All, Rest, ???, ???

Monthly food
""""""""""""
Each monthly food has an impact on your monster's stress, which varies based on the breed of monster.

.. csv-table:: Stress changes
    :header: Breed, Potato, Pasta, Turnip, Fish, Milk, Cup Jelly\*, Meat\*\*, Tablet, Tofu, Nothing

    Abyss, +30, 0, -10, -5, -60, -20, +30, -40, -30, +100
    Dulahan, +30, 0, +30, -5, -20, -10, -30, -60, -40, +100
    Hengar, +30, +30, -5, 0, -20, -30, -10, -60, -40, +100
    Tiger, -10, 0, -20, -5, -30, +30, -60, -40, +30, +100

**\*** Despite Cup Jelly's description saying it "promotes Fatigue relief", consuming it does not decrease fatigue.

**\*\*** Despite Meat's description saying it "relieves Stress when consumed", consuming it can cause the monster's stress to either decrease or increase depending on the monster's breed.

Impacts
-------

Lifespan
^^^^^^^^
Having a high stress and or fatigue will cause your monster to lose more lifespan each in-game week. For more details see :ref:`weekly lifespan decrease <weekly_lifespan_decrease>`.