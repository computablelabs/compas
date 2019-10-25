# compas
COMPutable AScii TUI

## Installation
#### Virtual environment
Note that we are assuming `pip` is installed and available

    which virtualenv || pip install --upgrade virtualenv

If you get an error above, you may need to use `sudo pip install virtualenv`.
With `virtualenv` installed, you can proceed:

    virtualenv -p python3 ~/compas_env

##### But I don't like that path...
Fine. You don't _have_ to use the above path (or name) for your virtualenv directory,
change it if you want, just substitute that name when appropriate.

##### Source it
Activate your environment before repository installation.

    source ~/compas_env/bin/activate

#### Repo
Clone the repository into wherever you do such things.

    cd <this/is/where>
    git clone git@github.com:computablelabs/compas.git
    cd compas
    pip install -r requirements.txt

## Use
Before firing up the ASCII UI Majesty that is *Compas*, you should do a couple things.

#### Export keys for a shell session
Compas will expect to be able to find `public_key` and `private_key` exported in
the running shell session. Note that your `private_key` is never exposed or broadcast
anywhere as Compas uses [Computable.py](https://github.com/computablelabs/computable.py/blob/master/computable/helpers/transaction.py#L49)
to sign transactions locally (offline) and then broadcast the signed transaction via its web3 provider.

So, open a terminal, then:

    export public_key=<0xXxx...>
    export private_key=<Xxx...>

Done correctly, `echo $public_key` and `$echo $private_key` will show the proper values.

### Fire it up
From the root of the repository (/compas/):

    python compas.py

## Asciimatics
Their docs on [User Interfaces](https://asciimatics.readthedocs.io/en/stable/widgets.html) has some handy information
until we put together some instructions inside the Compas app itself.
