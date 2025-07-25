.. _items:

Items
=====
There are several different types of items that you can get in-game. Items fall into the following categories:

* :ref:`Condition-changing <condition_changing_items>` - Increase or decrease things such as stress, fatigue, discipline, etc.
* :ref:`Passive effect <passive_effect_items>` - Passively decrease stress and/or fatigue
* :ref:`Stat-increasing <stat_increasing_items>` - Permanently increase particular stats
* :ref:`Temporary boosts <temporary_boosts>` - Temporarily increase battle stats or training effect, but reduce lifespan
* :ref:`Lifespan-increasing <lifespan_increasing_items>` - Increase lifespan
* :ref:`Combination <combination_items>` - Use when combining to change the resulting species
* :ref:`Valuable <valuable_items>` - Can be sold for a lot of gold

You can have up to 50 items in your inventory if you have the largest house size.

.. _item_preferences:

Preferences
-----------
The effects of items will vary slightly based on your monster's preferences. They may increase or decrease values a bit more than usual, and they might also impact other conditions the items does not usually impact.

For example, a monster that dislikes Elixir may result in :code:`-4` discipline, :code:`+3` wit, and :code:`-3` trust in addition to the item's normal :code:`-100` stress and :code:`+2` shape.

Each monster has a liked item and disliked item, however these are not the only items that the monster has preferences for or against.

.. _condition_changing_items:

Condition-changing
------------------
Condition-changing items are items that can be used in order to change your monster's :ref:`stress <stress>`, :ref:`fatigue <fatigue>`, discipline, shape, wit, or fame.

.. csv-table::
    :header: Name, Stress, Fatigue, Discipline, Shape, Wit, Fame, Cost

    Banana Ring, , -30, +5, +2, , , 200
    Medicinal Herb, , -100, +2, -2, , , 500
    Honey Shroom, , -300, -5, +2, , , 1000
    Monster Candy, -30, , +5, +2, , , 200
    Elixir, -100, , , +2, , , 500
    Sea Angel, -200, , -5, -2, , , 800
    Soda Lozenge, , , , +5, +20, , 600
    Worm Fungus, , , , -5, -20, , 600
    Roll Cake, , , +20, +5, , , 500
    Shock Rock, , , -20, -5, , , 500
    Fatty Meat, , +50, , +10, , , 200
    Blade Weed, +100, , , -20, , , 400
    Rosemoon, , , +5, , , +10, 2000

Passive effect
--------------
Passive effect items are items that passively reduce the stress or fatigue of your current monster.

Depending on the particular item, they either take effect at the start or each month or when resting. Many only take effect during specific seasons.

They are obtained by winning specific tournaments.

.. csv-table::
    :header: Name, Season, Trigger, Stress dec., Fatigue dec., Tournament

    Sculpture, All, Monthly, , ???, Artemis Cup (D 9/1)
    Gemini's Pot, All, Monthly, ???, , Gemini Cup (D 6/1)
    Weather Doll, Spring, Monthly, , ???, Rainbow Cup (D 8/3)
    Ice Cube, Summer, Monthly, ???, , Platinum Memorial (B 9/1)
    Cricket Chime, Autumn, Monthly, ???, , Cricket Cup (C 9/1)
    Fire Stone, Winter, Monthly, , ???, Treasure Cup (A 2/3)
    Music Box, All, Rest, ???, ???, Master Cup (S 10/4)

.. _stat_increasing_items:

Stat-increasing
---------------
Stat-increasing items increase a particular stat of your monster by :code:`2` when used.

.. csv-table::
    :header: Name, Stat, Effect, Shape, Trust

    Pow. Fruit, Power, +2, -1, +2
    Int. Fruit, Intelligence, +2, -1, +2
    Skil. Fruit, Skill, +2, -1, +2
    Spd. Fruit, Speed, +2, -1, +2
    Def. Fruit, Defense, +2, -1, +2
    Lif. Fruit, Life, +2, -1, +2

.. _temporary_boosts:

Temporary boosts
----------------
Temporary boost items temporarily increase your monsters stat in battle or stat increase through training for 1 week. Using them comes at the cost of decreasing your monster's lifespan.

Battle stats
^^^^^^^^^^^^
.. csv-table::
    :header: Name, Stats, Effect, Lifespan, Discipline, Trust

    Soybean Flour, Power & Intelligence, ???, -30, -15, -15
    Dragon Scale, Defense & Life, ???, -25, -10, -10
    Hot Lozenge, Skill & Speed, ???, -25, -10, -10

Training
^^^^^^^^
.. csv-table::
    :header: Name, Stats, Effect, Lifespan, Discipline, Trust

    Spook Bug, Power & Intelligence, ???, -30, -15, -15
    Red Mango, Defense & Life, ???, -25, -10, -10
    Bell Flower, Skill & Speed, ???, -25, -10, -10

.. _lifespan_increasing_items:

Lifespan-increasing
-------------------
Lifespan-increasing items are rare items that can be used to increase your monster's :ref:`lifespan <lifespan>`.

.. csv-table::
    :header: Name, Lifespan, Trust

    Silver Peach, +250, +10
    Gold Peach, +500, +20

.. _combination_items:

Combination items
-----------------
Combination items are items that can be used when combining two monsters in order to change the species of the resulting monster.

They are obtained when unlocking the ability to create a new monster species.

.. csv-table::
    :header: Name, Species

    King's Proof, Xenon
    Dragon Fang, Dragon
    Twin Edge, Durahan
    Fire Feather, Pheonix
    Cursed Mask, Joker
    Ancient Weapon, Hengar
    Gali Mask, Gali
    Knight's Lance, Centaur
    Naga Scale, Naga
    Black Slate, Monol
    Pupa, Beaclon

.. _valuable_items:

Valuable items
--------------
Valuable items are items that can be sold at the market for a lot of gold. Typically they are obtained as tournament prizes or on errantry.

.. csv-table::
    :header: Name, Sell price

    Silver Nugget, 5000
    Gold Nugget, 10000
    Platinum, 30000