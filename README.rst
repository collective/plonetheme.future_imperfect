.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
Future Imperfect
==============================================================================

Another fine responsive site template by html5 up, customized for Plone.

.. image:: https://raw.githubusercontent.com/vikas-parashar/plonetheme.future_imperfect/master/preview.png

Installation
------------

Zip
~~~~~~~~

#. Download the `zip file`_
#. Import the theme from the Diazo theme control panel.

Buildout
~~~~~~~~

Install ``plonetheme.future_imperfect`` by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plonetheme.future_imperfect


and then running ``bin/buildout``


Demo
-----

   This theme can be seen in action at the following site:

-  `Future Imperfect Theme Demo`_

Documentation
-------------

Full documentation for end users can be found `here`_

Contribution
-------------

- Clone the repo.
- Run ``bin/buildout``
- next, install the local dependencies theme requires
    ``$ npm install``
- Watch For Changes & Automatically Refresh
    ``$ grunt watch``
- Build & Optimize(This will create a ``dist`` folder with optimized files and a zip of theme)
    ``$ grunt dist``

License
-------

MIT License

Credit
------

Based on `Future Imperfect`_ Provided by `HTML5 UP`_

.. _zip file: https://github.com/vikas-parashar/plonetheme.future_imperfect/blob/master/plonetheme.future_imperfect.zip?raw=true
.. _Future Imperfect Theme Demo: http://107.170.136.197:8080/future-imperfect
.. _Future Imperfect: https://html5up.net/future-imperfect
.. _HTML5 UP: https://html5up.net/
.. _here: https://github.com/vikas-parashar/plonetheme.future_imperfect/blob/master/docs/index.rst