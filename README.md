# hovercraft-template
A template for [hovercraft] offering a reasonable default configuration for beautiful presentations

## Features
In addition to the features introduced by [hovercraft], this templates adds support for:
* Title page style using 4 different headings (title, subtitle, presenter, affiliation)
* Easy inclusion of corporate logos on the title page
* [Slide numbers](https://github.com/regebro/hovercraft/pull/108) (enabled by default, use ```:hide-slide-numbers: true``` in the document header to disable them)
* Visually appealing fonts and font sizes, compatible with most common screen sizes
* Open links in new tabs instead of the current one
* Showing one list item at a time on selected slides
  * In the console, all items are shown immediately so the presenter knows what will appear

## License
This template is based on the default template from [hovercraft] and uses the same license (MIT).

[hovercraft] and the original template are © Lennart Regebro

## How to use
This is a small sample presentation using all features introduced by this template. For more information about [hovercraft] and its multitude of features, check the [repository][hovercraft].

``` rst
:title: Presentation title

:logos: corporation.svg
        project.png
        
.. Use ':hide-slide-numbers: true' here to disable slide numbers

----

:id: title

Presentation title
==================

Presentation subtitle
---------------------

Author Name, Co-Author Name
:::::::::::::::::::::::::::

Author affiliations
...................

----

Slide title
===========

Slide text. This `link <https://www.github.com>`_ will be opened in another tab.


----

:class: oneatatime

One-at-a-time Slide
===================

* List items on this page
* Will appear

  * One at a time
  
* Once shown, they will stay until the page is reloaded. This should help navigating through the slideshow e.g. when answering questions afterwards.

.. note::

    As you can see, all items are immediately shown in the presenter console so the presenter always knows what's coming next.
    
    For the moment, this only works if the window with the presentation is focused. If the console is focused, it doesn't work (yet).

```

And [here](https://www.die-sinlosen.de/hovercraft-template-demo/) is how it looks.

[hovercraft]: https://github.com/regebro/hovercraft
