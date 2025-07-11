Lifespan
========
Each monster has a lifespan which determines how much longer it has to live. Stress, fatigue, battles, and the inevitable progression of time will lower a monster's remaining lifespan.

Once a monster's lifespan reaches :code:`0`, they will die.

Weekly decrease
---------------
At the start of every in-game week, your current monster's lifespan decreases by a base amount of :code:`10`. Their lifespan is then further decreased based on the monster's current stress and fatigue.

.. csv-table::
    :header: "Stress", "Lifespan decrease"

    0 to 299, 0
    300 to 499, 2
    500 to 699, 6
    700 to 899, 14
    900 and higher, 22

.. csv-table::
    :header: "Fatigue", "Lifespan decrease"

    0 to 299, 0
    300 to 499, 2
    500 to 699, 6
    700 to 899, 14
    900 and higher, 22

So for example, if your monster has a stress level of :code:`50` and a fatigue level of :code:`350` then your monster's lifespan will decrease by :code:`12` (:code:`10 + 0 + 2`).

In the worst case, your monster can lose as much as :code:`52` lifespan in a single in-game week (with 900+ stress and 900+ fatigue).