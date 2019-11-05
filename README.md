ImageSearchLibrary is a library dedicated to GUI management.
========================================================

DISCLAIMER: The biggest part of the work has been done by Martin Lees.
Follow this link to see his work: https://github.com/drov0.

This module is a rework of Martin Lees' work to offer a solution for Robot Framework.

It can be installed using pip:
    pip install ImageSearchLibrary

With this module you will be able to do the basics of image recognition using RF.

The keywords created can be found in the << core.py >> module in the << __all__ >> variable
at the beginning of the file.

Image recognition example in Robot Framework:

    ${img}=     Set Variable                        .${/}google.png
    ${pos}=     ImageSearchLibrary.Search Image     ${img}
    ImageSearchLibrary.Click Image                  ${img}              ${pos}

Is the top example, the image searched in the Google logo.
If found, the << pos >> variable gets the coordinates of the top-left corner of the found image.
Once you get the position, you can click on the image.
The << Click Image >> keyword needs the image to calculate the middle of it.

Focus window example in Robot Framework:
    ImageSearchLibrary.Focus Window     

Exemple d'usage:

    >>> from sm_lib import proclamer
    >>> proclamer()

Ce code est sous licence WTFPL.
