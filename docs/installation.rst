How To Run?
==========

Note that this is currently a work in progress. So things may not work as you
expected it to work. If you want to test this you need to have following installed
on your system

* pip
* Virtualenv

Test deployment

.. code-block:: shell-session

    $ git clone https://github.com/Project-SILPA/Silpa-Flask.git
    $ cd Silpa-Flask
    $ pip install -r requirements.txt
    $ python silpa.py

If you want to Install all modules:

.. code-block:: shell-session

    $ pip install -r modules.txt

Or you can Install modules manually

* `Soudex  <https://github.com/Project-SILPA/Soundex>`_
* `ApproxSearch <https://github.com/Project-SILPA/ApproxSearch>`_
* `Transliteration <https://github.com/Project-SILPA/Transliteration>`_
* `Spellchecker <https://github.com/Project-SILPA/spellchecker>`_
* `Hyphenation <https://github.com/Project-SILPA/Hyphenation>`_
* `Chardetails <https://github.com/Project-SILPA/chardetails>`_
* `Payyans <https://github.com/Project-SILPA/payyans>`_

Currently only these modules are used but you can include more you can
find some more modules in `Project-SIlpa
<https://github.com/Project-SILPA>`_ Github account, install them and
add a line in *silpa.conf* for enabling them.

Additionally we would need a *normalizer* module for *Transliteration* modules correct working.
Get it from below URL and install it in your virtual environment but

.. warning::

 Do not add a line to silpa.conf  for this module. Its not a web module pure python module

VirtialEnv Instructions
-----------------------

If you are on Mac OS X or Linux, chances are that one of the following two commands will work for you:

.. code-block:: shell-session

 $ sudo easy_install virtualenv

or even better:

.. code-block:: shell-session

 $ sudo pip install virtualenv

One of these will probably install virtualenv on your system. Maybe it’s even in your package manager. If you use Ubuntu, try:

.. code-block:: shell-session

 $ sudo apt-get install python-virtualenv

Once you have virtualenv installed, just fire up a shell-session and create your own environment.

.. code-block:: shell-session

 $ git clone git://github.com/copyninja/Silpa-Flask.git
 $ cd Silpa-Flask
 $ virtualenv silpa

 New python executable in silpa/bin/python
 Installing distribute............done.


Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:

.. code-block:: shell-session

 $ . silpa/bin/activate

If you are a Windows user, the following command is for you:

.. code-block:: shell-session

 $ silpa\scripts\activate.bat

Either way, you should now be using your virtualenv (notice how the prompt of your shell-session has changed to show the active environment).

Now you can just enter the following command to get Flask activated in your virtualenv:

.. code-block:: shell-session

 $ pip install Flask

A few seconds later and you are good to go.

You can start the silpa application by
.. code-block:: shell-session

 python silpa.py
 Running on http://127.0.0.1:5000/

Well not exactly. You will see error messages saying Failed to import module xyz. That means you need to install the modules.
Here is an example module installation for Soundex. Repeat this for other modules.

.. code-block:: shell-session

 mkdir modules
 cd modules
 git clone git://github.com/copyninja/Soundex.git
 cd Soundex
 python setup.py install

And restart the server by just killing and running python silpa.py again.
