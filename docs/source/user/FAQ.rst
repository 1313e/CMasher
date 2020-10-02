.. _FAQ:

FAQ
===
Can/How do I request a colormap?
--------------------------------
Users can request for a specific colormap to be made, by opening a `GitHub issue`_ and using the `Colormap request` template.
In this issue, one can supply me with the colors, style and (preferably) test data, and I will try to create a colormap that satisfies your requirements.
Colormaps made through this system might end up becoming *CMasher* colormaps themselves if I believe they are universally applicable, or else I will provide the source files of the colormap itself in case they are too specific for a use-case.
Please note that I cannot guarantee that I can design a colormap that fully satisfies your requirements (as it might be impossible to do so), but I will always try to create one that you like.

.. _repository: https://github.com/1313e/CMasher
.. _GitHub issue: https://github.com/1313e/CMasher/issues


Can I add my own colormaps?
---------------------------
I am always open for ideas, so I definitely recommend opening an issue about it and showing what you have.
However, I am particularly picky when it comes to designing and adding colormaps, and especially about naming them, so I cannot guarantee that I will accept a colormap to be added.


Can I request a colormap utility feature?
-----------------------------------------
Definitely.
*CMasher* is about providing scientific colormaps AND the tools for using them properly.
If you have an idea for a utility feature (like a function; class; CLI-command; etc.) that is related to using colormaps, please open a `GitHub issue`_ using the `Feature request` template.


There are artifacts in a *CMasher* colormap
-------------------------------------------
All colormaps in *CMasher* are as close to perceptually uniform sequential as they can be without significantly lowering its quality.
I always try to make sure that the error in the uniformity is much lower than what the human eye can distinguish.
The colormaps should therefore not contain any visible artifacts (but do open a `GitHub issue`_ if you believe there truly is an artifact).

However, screens are not always capable of showing every single color exactly the way they are.
Some screens for example, can have trouble showing specific shades of red, showing a slightly different shade instead.
This can cause these screens to show a *CMasher* colormap with what seems to be an artifact, even though the artifact is not there and would vanish when viewed on a different screen.
Common color artifacts that I have noticed in screens include shades of red or green not showing properly, and dark purple showing up as pure black.

A funny side effect of this is that some colormaps, like :ref:`chroma`; :ref:`rainforest`; :ref:`neon`; and :ref:`pride`, are great for testing the color performance of a screen.
Simply view their `viscm` outputs on a screen (which can be found on the individual colormap pages), and any problems should immediately show up.