
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

End of a month
^^^^^^^^^^^^^^

Tournaments
^^^^^^^^^^^
Participating in a tournament decreases that monster's stress but increases their fatigue.

Items
^^^^^
There are several items that impact stress and fatigue. These are broken down into three categories:

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

    Sculpture, All, Daily, , ???
    Gemini's Pot, All, Daily, ???,
    Weather Doll, Spring, Daily, , ???
    Ice Cube, Summer, Daily, ???,
    Cricket Chime, Autumn, Daily, ???,
    Fire Stone, Winter, Daily, , ???
    Music Box, All, Rest, ???, ???

Monthly food
""""""""""""

.. csv-table::
    :header: Name, Stress change

    Potato, +30
    Pasta, +30
    Turnip, -5
    Fish,
    Milk, -20
    Cup Jelly \*, -30
    Meat, -10
    Tablet, -60
    Tofu, -40
    Nothing, +100

\* Despite Cup Jelly's description saying it "promotes Fatigue relief", consuming it does not decrease fatigue.

.. note::

    The above stat changes were found by feeding the food to a Hengar. The impact may vary based on monster breed.

Impacts
-------

Lifespan
^^^^^^^^
Having a high stress and or fatigue will cause your monster to lose more lifespan each in-game week. For more details see :ref:`weekly lifespan decrease <weekly_lifespan_decrease>`.