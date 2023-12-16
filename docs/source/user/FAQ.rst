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


The edges of white-centered diverging colormaps are too similar
---------------------------------------------------------------
Some diverging colormaps in *CMasher*, like :ref:`fusion` and :ref:`waterlily`, have a white center and linearly decrease to :math:`10\%` lightness at the edges.
Depending on the screen that is being used and who is looking at the colormap, this may make it difficult to distinguish the two edges from each other.
The reason for this is that white-centered diverging colormaps should normally be used for plots where the central values are the main focus of the plot, like probability maps (the lower the number of standard deviations, the better).
Therefore, the edge values should have very little importance, and thus should look similarly dark.
When plotting values where the deviation from the center should be highlighted, for example with radial velocity maps or for showing probability outliers, one should normally use a black-centered diverging colormap, like :ref:`iceburn`; :ref:`redshift`; or :ref:`wildfire`.

However, when it is not possible/desirable to use a black-centered diverging colormap and the edges should be distinguishable, one can easily solve this by cutting away a small fraction at the edges of the desired colormap using the :func:`~cmasher.get_sub_cmap` function.
For example, :pycode:`cmr.get_sub_cmap('cmr.fusion', 0.05, 0.95)` will cut away :math:`5\%` at each side of the :ref:`fusion` colormap.
See :ref:`sub_colormaps` for more details on the usage of this function.


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


Why are there so many diverging colormaps with a blue end?
----------------------------------------------------------
There are two reasons for this: Ease-of-use and CVD-friendliness.
The color blue (and surrounding shades of purple and blue-green) takes up a very large volume in colorspace.
This means that it is really easy to create a perceptually uniform track through colorspace that involves blue.
The sheer number of blue sequential colormaps in *CMasher* show this as well, with :ref:`cosmic`; :ref:`arctic`; :ref:`freeze`; :ref:`voltage`; :ref:`ocean`; and :ref:`gem` all primarily using the color blue.
Their *viscm* outputs also show how wide the arcs through colorspace can be without including other major colors (besides purple).

The more important reason however, is that blue is very CVD-friendly.
Unlike most other colors, blue appears as blue to pretty much everyone, including those that are affected by CVD, and is usually the only color to appear as blue for people with CVD as well.
When making colormaps, I usually try to make sure that they are CVD-friendly (i.e., people with CVD can still perceive and interpret a plot with a CVD-friendly colormap properly).
Of course, there are some examples of colormaps that are not CVD-friendly, like :ref:`chroma`; :ref:`neon`/:ref:`tropical`; :ref:`wildfire`; and :ref:`seasons`, but their pages mention this and these colormaps were purely made to have an exceptionally high perceptual range.

For sequential colormaps, I can use colors that end up having the same saturation for people with CVD, as long as their lightness values are distinctively different.
A great example of this is :ref:`savanna`, which is a sequential colormap that is CVD-friendly despite using solely green and red.
The *viscm* output of :ref:`savanna` shows that the colormap becomes a yellow-only colormap for the most common types of CVD, which still works just fine.

For diverging colormaps however, using this 'trick' is no longer possible.
Diverging colormaps require the use of distinctive sequential colormaps on both sides, which must also be true when viewed by a person affected by CVD.
For this reason and because of the properties of blue I mentioned above, I tend to end up using blue for one end of every diverging colormap.
The only two diverging colormaps in *CMasher* that do not have a blue end (at time of writing), are :ref:`holly` and :ref:`watermelon`.
One look at the *viscm* output of :ref:`watermelon` tells you immediately that this colormap will not work well for CVD-friendly plots, as both sides end up looking very similar.

Of course, it is possible to make diverging colormaps without blue that are still CVD-friendly.
However, these colormaps usually tend to end up looking very boring and dull, as I have to prioritize using CVD-friendly colors over colorful colors.
And while this could be useful, this also means that they end up having low perceptual ranges, which kind of defeats the entire purpose of a diverging colormap.
