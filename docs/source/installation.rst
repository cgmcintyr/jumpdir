Installation
============

Simply

::
    ``pip install jumpdir``

    or

    ``pip3 install jumpdir``

And add the following function to your .bashrc file

.. code-block:: bash
    
    function jd {
        TARGET="$(jumpdir search $@)"

        if [ $TARGET != "None" ]; then
            cd $TARGET
        else
            echo "Jumpdir could not find a matching directory :("
        fi
    }

