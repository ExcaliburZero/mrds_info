.. _lifespan:

Lifespan
========
Each monster has a lifespan which determines how much longer it has to live. Stress, fatigue, tournaments, and the inevitable progression of time will lower a monster's remaining lifespan.

Once a monster's lifespan reaches :code:`0`, they will die.

.. _weekly_lifespan_decrease:

Weekly decrease
---------------
At the start of every in-game week, your current monster's lifespan decreases by a base amount of :code:`10`. Their lifespan is then further decreased based on the monster's current :ref:`stress <stress>` and :ref:`fatigue <fatigue>`.

.. csv-table::
    :header: "Stress", "Lifespan decrease"

    0 to 299, 0
    300 to 499, 2
    500 to 699, 6
    700 to 899, 14
    900 to 999, 22

.. csv-table::
    :header: "Fatigue", "Lifespan decrease"

    0 to 299, 0
    300 to 499, 2
    500 to 699, 6
    700 to 899, 14
    900 to 999, 22

So for example, if your monster has a stress level of :code:`50` and a fatigue level of :code:`350` then your monster's lifespan will decrease by :code:`12` (:code:`10 + 0 + 2`).

In the worst case, your monster have its lifespan decrease by as much as :code:`52` in a single in-game week (with :code:`900+` stress and :code:`900+` fatigue).

Tournaments
-----------
Having your monster participate in a tournament reduces its lifespan. Losing a tournament decreases your monster's lifespan by :code:`24`, while winning a tournament only reduces their lifespan by :code:`8`.

.. note::

    The lifespan decrease for tournaments definitely is impacted by win/loss, but I'm not sure yet if there are other factors that impact it.

Items
-----
There are several consumable items that impact your monster's lifespan. They are grouped into the following categories:

* Items that decrease lifespan as a tradeoff for temporary battle stat or training effectiveness increases
* Items that increase lifespan

Decrease
^^^^^^^^
.. csv-table::
    :header: "Name", "Type", "Stats", "Lifespan decrease"

    Soybean Flour, Battle+, Power & Intelligence, 30
    Dragon Scale, Battle+, Defense & Life, 25 
    Hot Lozenge, Battle+, Skill & Speed, 25
    Spook Bug, Training+, Power & Intelligence, 30
    Red Mango, Training+, Defense & Life, 25
    Bell Flower, Training+, Skill & Speed, 25

Increase
^^^^^^^^
There are two rare items that can increase your monster's lifespan: Silver Peach and Gold peach. Lifespan maxes out at :code:`9999`, so increasing your monsters lifespan can have it exceed it's original lifespan at creation.

.. csv-table::
    :header: "Name", "Lifespan increase"

    Silver Peach, 250
    Gold Peach, 500
