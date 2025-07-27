.. _lifespan:

Lifespan
========
Each monster has a lifespan which determines how much longer it has to live. Stress, fatigue, tournaments, and the inevitable progression of time will lower a monster's remaining lifespan.

When a monster's starts a week with its lifespan at :code:`0`, they will die.

Cleo's warning
--------------
Cleo will warn you when your monster's lifespan drops below 25% of its starting lifespan.

    Um, <PLAYER>? This isn't easy for me...

    But maybe it's time to let <MONSTER> go.

    It's starting to slow down, and...I think it's just getting too old.

    The best thing to do would be freeze and combine it at the Lab.

Even when you get this warning, you still have quite a bit of time left with your monster. Depending on your monster's starting lifespan, they may have ~8 months to ~1 year and 4 months of lifespan left.

Factors
-------
There are several things that impact a monster's lifespan:

* :ref:`Time passing <weekly_lifespan_decrease>` causes your monster's lifespan to decrease based on its stress and fatigue
* :ref:`Going on drills and errantry <lifespan_drills_and_errantry>` impacts lifespan slightly differently than training and resting
* :ref:`Participating in tournaments <lifespan_tournaments>` decreases your monster's lifespan
* :ref:`Certain items <lifespan_items>` can increase or decrease your monsters lifespan

.. _weekly_lifespan_decrease:

Weekly decrease
^^^^^^^^^^^^^^^
At the start of every week, your current monster's lifespan decreases by a base amount of :code:`10`. Their lifespan is then further decreased based on the monster's current :ref:`stress <stress>` and :ref:`fatigue <fatigue>`.

.. csv-table::
    :header: Stress, Lifespan

    0 to 299, 0
    300 to 499, -2
    500 to 699, -6
    700 to 899, -14
    900 to 999, -22

.. csv-table::
    :header: Fatigue, Lifespan

    0 to 299, 0
    300 to 499, -2
    500 to 699, -6
    700 to 899, -14
    900 to 999, -22

So for example, if your monster has a stress level of :code:`50` and a fatigue level of :code:`350` then your monster's lifespan will decrease by :code:`12` (:code:`10 + 0 + 2`).

In the worst case, your monster have its lifespan decrease by as much as :code:`52` in a single week (with :code:`900+` stress and :code:`900+` fatigue).

.. _lifespan_drills_and_errantry:

Drills & errantry
^^^^^^^^^^^^^^^^^
When you send your monster on a drill or errantry, while the activity takes 4 weeks, only 2 weeks worth of :ref:`weekly lifespan decreases <weekly_lifespan_decrease>` are applied. The 2 decreases are applied based on your monster's stress and fatigue after coming back from the drill or errantry.

Because of this, **doing a drill or errantry can be a more effective use of lifespan than normal training**.

For example, if you monster returns from a drill with :code:`408` stress and :code:`436` fatigue then its lifespan will be decreased by :code:`28`. This is less than the decrease of :code:`40` that could occur if resting or training for 4 weeks.

.. _lifespan_tournaments:

Tournaments
^^^^^^^^^^^
Having your monster participate in a tournament reduces its lifespan. Losing a tournament decreases your monster's lifespan by :code:`24`, while winning a tournament only reduces their lifespan by :code:`8`.

Your monster's stress and fatigue do not have any impact on how much lifespan they lose due to participating in tournaments.

.. _lifespan_items:

Items
^^^^^
There are several consumable items that impact your monster's lifespan. They are grouped into the following categories:

* Items that decrease lifespan as a tradeoff for temporary battle stat or training effectiveness increases
* Items that increase lifespan

Decrease
""""""""
.. csv-table::
    :header: Name, Type, Stats, Lifespan

    Soybean Flour, Battle+, Power & Intelligence, -30
    Dragon Scale, Battle+, Defense & Life, -25 
    Hot Lozenge, Battle+, Skill & Speed, -25
    Spook Bug, Training+, Power & Intelligence, -30
    Red Mango, Training+, Defense & Life, -25
    Bell Flower, Training+, Skill & Speed, -25

Increase
""""""""
There are two rare items that increase your monster's lifespan: :ref:`Silver Peach and Gold Peach <lifespan_increasing_items>`. Lifespan maxes out at :code:`9999`, so increasing your monsters lifespan can have it exceed it's original lifespan at creation.

.. csv-table::
    :header: Name, Lifespan

    Silver Peach, +250
    Gold Peach, +500

The monthly food Tofu has the impact of increasing your monster's lifespan by :code:`5`.

.. csv-table::
    :header: Name, Lifespan

    Tofu, +5

Starting lifespan
-----------------
Each monster species starts out with a particular lifespan when it is created. Even for species with the same main-breed, their lifespan will vary based on their sub-breed.

The pattern for the lifespan of a given breed depending on its sub-breed appears to be the following:

* For sub-breeds that are not "?", the monster's starting lifespan is 60/40 the starting lifespans of the pure-breed versions of the main and sub-breeds. [#f1]_ [#f2]_
* For "-ish" monsters, their starting lifespan is 105% of the pure-breed.
* For special "?" monsters, their starting lifespan is 90% of the pure-breed.

As some examples of how to calculate the lifespans:

* Falco / Abyss has a lifespan of :code:`0.6 * 1900 + 0.4 * 2050` = :code:`1140 + 820` = :code:`1960`
* Falco / ? (-ish) has a lifespan of :code:`1900 * 1.05` = :code:`1995`
* Falco / ? (Jock) has a lifespan of :code:`1900 * 0.90` = :code:`1710`

The table below shows the 7 types of Falco in comparison to their sub-breed lifespans.

.. csv-table::
    :header: Breeds, Main, Sub, Lifespan

    Falco / Falco, 1900, 1900, 1900
    Falco / Abyss, 1900, 2050, 1960
    Falco / Ogyo, 1900, 2050, 1960
    Falco / Mew, 1900, 2000, 1940
    Falco / Piroro, 1900, 2200, 2020
    Falco / ? (-ish), 1900, \-, 1995
    Falco / ? (Jock), 1900, \-, 1710

Pure-breed lifespans
^^^^^^^^^^^^^^^^^^^^
Below are the starting lifespans of the pure-breed species.

.. csv-table::
    :header: Breed, Lifespan, Estimated age\*

    Abyss,2050,"4 years, 3 months"
    Baku,2100,"4 years, 4 months"
    Beaclon,2050,"4 years, 3 months"
    Centaur,1950,"4 years, 0 months"
    Color Pandora,2000,"4 years, 2 months"
    Dragon,1850,"3 years, 10 months"
    Ducken,1950,"4 years, 0 months"
    Durahan,2100,"4 years, 4 months"
    Falco,1900,"3 years, 11 months"
    Gali,1700,"3 years, 6 months"
    Golem,2300,"4 years, 9 months"
    Hare,2000,"4 years, 2 months"
    Hengar,2500,"5 years, 2 months"
    Joker,1500,"3 years, 1 months"
    Lesione,2500,"5 years, 2 months"
    Mew,2000,"4 years, 2 months"
    Mocchi,2000,"4 years, 2 months"
    Monol,1800,"3 years, 9 months"
    Naga,1750,"3 years, 7 months"
    Ogyo,2050,"4 years, 3 months"
    Pancho,2150,"4 years, 5 months"
    Pheonix,1500,"3 years, 1 months"
    Piroro,2200,"4 years, 7 months"
    Pixie,1900,"3 years, 11 months"
    Plant,2000,"4 years, 2 months"
    Suezo,1950,"4 years, 0 months"
    Tiger,1950,"4 years, 0 months"
    Xenon,2250,"4 years, 8 months"
    Zan,1850,"3 years, 10 months"

\* Assumes no lifespan loss beyond weekly decrease (ex. if resting every week). Actual number of years and months of life will likely be lower by a few months.

Special cases
^^^^^^^^^^^^^
There are four monsters that do not follow the normal lifespan calculations:

.. csv-table::
    :header: Breed, Lifespan

    Geemo, 2520
    XBakuBaku, 2100
    XPalco, 2280
    Woodie, 1850

.. rubric:: Footnotes

.. [#f1] Thanks to Monster Fenrick (Taylor W) on the /r/monsterrancher chat Discord server for pointing out that the lifespan for mixed-breeds might be 60/40 the main and sub-breeds' lifespan.
.. [#f2] A different, but equivalent, approach to calculating mixed-breed monster lifespans is described in `Penopat's GameFAQs thread <https://gamefaqs.gamespot.com/boards/946519-monster-rancher-ds/56024426>`_.