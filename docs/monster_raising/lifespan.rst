.. _lifespan:

Lifespan
========
Each monster has a lifespan which determines how much longer it has to live. Stress, fatigue, tournaments, and the inevitable progression of time will lower a monster's remaining lifespan.

When a monster's starts a week with its lifespan at :code:`0`, they will die.

.. _weekly_lifespan_decrease:

Weekly decrease
---------------
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

Drills & errantry
-----------------
When you send your monster on a drill or errantry, while the activity takes 4 weeks, only 2 weeks worth of :ref:`weekly lifespan decreases <weekly_lifespan_decrease>` are applied. The 2 decreases are applied based on your monster's stress and fatigue after coming back from the drill or errantry.

Because of this, **doing a drill or errantry can be a more effective use of lifespan than normal training**.

For example, if you monster returns from a drill with :code:`408` stress and :code:`436` fatigue then its lifespan will be decreased by :code:`28`. This is less than the decrease of :code:`40` that could occur if resting or training for 4 weeks.

Tournaments
-----------
Having your monster participate in a tournament reduces its lifespan. Losing a tournament decreases your monster's lifespan by :code:`24`, while winning a tournament only reduces their lifespan by :code:`8`.

Your monster's stress and fatigue do not have any impact on how much lifespan they lose due to participating in tournaments.

Items
-----
There are several consumable items that impact your monster's lifespan. They are grouped into the following categories:

* Items that decrease lifespan as a tradeoff for temporary battle stat or training effectiveness increases
* Items that increase lifespan

Decrease
^^^^^^^^
.. csv-table::
    :header: Name, Type, Stats, Lifespan

    Soybean Flour, Battle+, Power & Intelligence, -30
    Dragon Scale, Battle+, Defense & Life, -25 
    Hot Lozenge, Battle+, Skill & Speed, -25
    Spook Bug, Training+, Power & Intelligence, -30
    Red Mango, Training+, Defense & Life, -25
    Bell Flower, Training+, Skill & Speed, -25

Increase
^^^^^^^^
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
    :header: Breed, Lifespan

    Abyss, 2050
    Baku, 2100
    Beaclon, 2050
    Centaur, 1950
    Color Pandora, 2000
    Dragon, 1850
    Ducken, 1950
    Durahan, 2100
    Falco, 1900
    Gali, 1700
    Golem, 2300
    Hare, 2000
    Hengar, 2500
    Joker, 1500
    Lesione, 2500
    Mew, 2000
    Mocchi, 2000
    Monol, 1800
    Naga, 1750
    Ogyo, 2050
    Pancho, 2150
    Pheonix, 1500
    Piroro, 2200
    Pixie, 1900
    Plant, 2000
    Suezo, 1950
    Tiger, 1950
    Xenon, 2250
    Zan, 1850

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