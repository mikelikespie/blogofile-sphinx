:title:         Hello World
:post_date:     2009/09/21 10:05:17
:tags:          blogofile
:categories:    Software
:author:        Mike Lewis

Hi, this is my first post. I decided to start a project about a week ago to
write my own blogging software that used some of my favorite technologies
including `Mako <http://makotemplates.org>`_, Git, and rST/`Sphinx
<http://sphinx.pocoo.org>`_. A colleague of mine pointed me to `Blogofile
<http://www.blogofile.com/>`_ which had most of what I wanted aside from the
rST/Sphinx integration.

Hacked on it a bit over my vacation this weekend and finally have something
working.  It's certainly not ready for the mainstream yet. The following things
will require work:

Current Issues
^^^^^^^^^^^^^^
.. highlight:: rst

* Headings/Sections. No matter what I do, they convert into ``<h1/>`` tags if I
  only have on heading on a page
* Cross-referencing posts properly
* Image inclusions
* Ability to use ``:date:`` metadata tag instead of ``:post_date:`` (need to
  look into this)
* Getting rid of some spninx artifacts like the TOC, and the index file which
  aren't being used
* Would like to define the table such as ::

    Hello World
    ===========

  Instead of ``:title: Hello World``
    
* A tighter integration with Blogofile

I believe the latter will require a custom Sphinx builder. That will probably
fix most of the other problems too, but seems rather intensive right now.

Methodology
^^^^^^^^^^^
Currently, I am building with the ``JSONHTMLBuilder()`` by calling the
``Sphinx()`` class directly.

I then take the ``.fjson`` files and output them into ``.html`` format for
Blogofile, prepending the metadata as the standard ``YAML``.

Plans
^^^^^
Well, I am on a flight right now, and have to go straight to work, but when I
get home I suppose I will post a git repo of what I have so far as a proof of
concept.

I'd also like to convert my current wordpress blog to blogofile ASAP and put
this on the internet.

The Sphinx Advantage
^^^^^^^^^^^^^^^^^^^^
Some of you who are familiar with Blogofile might be wondering why I'm going
through the effort of adding yet another wiki markup format to Blogofile when
there's already Markup and Textile (I believe). 

* I like Sphinx and am familiar with it
* It will work great for doing technical writeups.

  * Love the pygments integration (I know Blogofile has it)

  * Cross-referencing other projects documented in Sphinx

  * Including source files in postings instead of cutting & pasting snippets.

* Footnotes
* Easily extensible with custom directives

Before I start evangelizing it more, I will eat my own dogfood ``;)``.

Here's what some of this file looks like::

    :title:         Hello World
    :post_date:     2009/09/21 10:05:17
    :tags:          blogofile
    :categories:    Software
    :author:        Mike Lewis

    ....

    The Sphinx Advantage
    ^^^^^^^^^^^^^^^^^^^^
    Some of you who are familiar with Blogofile might be wondering why I'm going
    through the effort of adding yet another wiki markup format to Blogofile when
    there's already Markup and Textile (I believe). 

    * I like Sphinx and am familiar with it
    * It will work great for doing technical writeups.

      * Love the pygments integration (I know Blogofile has it)

    ....

    Here's what some of this file looks like::

        :title:         Hello World
        :post_date:     2009/09/21 10:05:17
        :tags:          blogofile
        :categories:    Software


Pretty meta, huh?


Other Plans for my Blogofile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
Albeit a ruby project, I am in *love* with `SASS <http://sass-lang.com/>`_. If
you're not familiar, it's pretty much programmable CSS. It almost makes CSS
tolerable. That's a bold claim I know, but try it.

With `Compass <http://github.com/chriseppstein/compass/tree/master>`_, it's
pretty easy to integrate into most projects. I'm currently using it in a couple
Pylons projects (blasphemy, I know).

It should only be a few minutes to throw it in here, but then I will be forced
to style it.
 
