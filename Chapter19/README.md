# Training a Custom Tesseract Model

However, we have yet to train/fine-tune a Tesseract model on our **custom dataset**.

As you’ll see, training a custom Tesseract model has absolutely **nothing to do with
programming and writing code** and instead involves:

1. Properly configuring your development environment with the required Tesseract training
tools
1. Structuring your OCR dataset in a manner Tesseract can understand
1. Correctly setting Tesseract environment variables in your shell
1. Running the correct Tesseract training commands

Suppose you’ve ever worked with [Caffe](https://github.com/BVLC/caffe) or [the TensorFlow Object Detection API](https://github.com/TensorFlow/models/tree/master/research/object_detection),
then you know these tools typically don’t require you to open an integrated development
environment (IDE) and write hundreds of lines of code.

Instead, they are far more focused on ensuring the dataset is correctly structured, followed by
issuing a series of (sometimes complicated) commands.

**Training a custom Tesseract model is the same** — and in the remainder of this chapter,
you will learn how to fine-tune a Tesseract model on a custom dataset.

## Learning Objectives
In this chapter, you will learn how to:
1. Configure your development environment for Tesseract training
1. Install the ``tesstrain`` package, which utilizes ``make`` files to construct training
commands and commence training easily
1.  Understand the dataset directory structure required when training a custom Tesseract
model
1. Review the dataset we’ll be using when training our Tesseract model
1. Configure the base Tesseract model that we’ll be training
1. Train the actual Tesseract OCR model on our custom dataset

## Your Tesseract Training Development Environment
If possible, I suggest using a virtual machine (VM) or a cloud-based instance the first time you 
configure a system to train a Tesseract model. The reasoning behind this suggestion is simple
— you *will* make a mistake once, twice, and probably even three times before you properly
configure your environment.

Configuring Tesseract to train a custom model for the first time is hard, so having an
environment where you can snapshot a base operating system install, do your work with
Tesseract, and when something goes wrong, instead of having to reconfigure your bare metal
machine, you can instead revert to your previous state.

### Step #1: Installing Required Packages
This section provides instructions to install operating-system-level packages required to:
1. compile Tesseract from source and
1. train custom OCR models with Tesseract.

Unfortunately, compiling Tesseract from source is a requirement to use the training utilities.
Luckily, installing our required packages is as simple as a few ``apt-get`` and ``brew`` commands.

##### Vagrant
We can use [vagrant](https://developer.hashicorp.com/vagrant/install?product_intent=vagrant) to stiumulate it .
1. This command creates and configures guest machines according to your Vagrantfile.
    ```
    vagrant up [name|id]
    ```
1. This command shuts down the running machine Vagrant is managing.
    ```
    vagrant halt [name|id]
    ```
1. This suspends the guest machine Vagrant is managing, rather than fully shutting it down or destroying it.
    ```
    vagrant suspend [name|id]
    ```
1. This resumes a Vagrant managed machine that was previously suspended, perhaps with the suspend command.
    ```
    vagrant resume [name|id]
    ```   
1. [This will SSH into a running Vagrant machine and give you access to a shell](https://developer.hashicorp.com/vagrant/docs/cli/ssh).
    ```
    vagrant ssh [name|id] [-- extra_ssh_args]
    ``` 
1. [This will output valid configuration for an SSH config file to SSH into the running Vagrant machine from ssh directly (instead of using vagrant ssh)](https://developer.hashicorp.com/vagrant/docs/cli/ssh_config).
    ```
    vagrant ssh-config [name|id]
    ```
1. [This command stops the running machine Vagrant is managing and destroys all resources that were created during the machine creation process. ](https://developer.hashicorp.com/vagrant/docs/cli/destroy).
    ```
    vagrant destroy [name|id]
    ```
##### Ubuntu
```bash
$ sudo apt-get install -y libicu-dev libpango1.0-dev libcairo2-dev
$ sudo apt-get install -y automake ca-certificates g++ git libtool libleptonica-dev make pkg-config
$ sudo apt-get install -y --no-install-recommends asciidoc docbook-xsl xsltproc
$ sudo apt-get install -y libpng-dev libjpeg8-dev libtiff5-dev zlib1g-dev
```
Assuming none of these commands error out, your Ubuntu machine should have the proper
OS-level packages installed.

##### macOS 
If you’re on a macOS machine, installing the required OS-level packages is almost as easy —
all we need is to use [Homebrew](https://brew.sh) and the ``brew`` command:
```bash
$ brew install -y icu4c pango cairo
$ brew install -y automake gcc git libtool leptonica make pkg-config
$ brew install -y libpng jpeg libtiff zlib
```
However, there is an additional step required. The ``icu4c`` package, which contains C/C++ and
Java libraries for working with Unicode, requires that we manually create a symbolic link
(sym-link) for it into our ``/usr/local/opt`` directory:
```bash
$ ln -hfs /usr/local/Cellar/icu4c/67.1 /usr/local/opt/icu4c
```
**⚠Note** that the current version (as of this writing) for ``icu4c`` is **67.1**. I suggest you use tab
completion when running the command above. New versions of ``icu4c`` will require the
command to be updated to utilize the correct version (otherwise, the path will be invalid, and
thus the sym-link will be invalid as well).

### Step #2: Building and Installing Tesseract Training Tools
Now that our OS-level packages are installed, we can move on to compiling Tesseract from
source, giving us access to Tesseract’s training utilities.

##### Ubuntu
On an Ubuntu machine, you can use the following set of commands to:
1. Download Tesseract v5.3.4
1. Configure the build
1. Compile Tesseract
1. Install Tesseract and it’s training utilities
The commands follow:
```bash
$ wget -O tesseract.zip https://github.com/tesseract-ocr/tesseract/archive/refs/tags/5.3.4.zip
$ unzip tesseract.zip
$ mv tesseract-5.3.4 tesseract
$ cd tesseract
$ ./autogen.sh
$ ./configure
$ make
$ sudo make install
$ sudo ldconfig
$ make training
$ sudo make training-install
```
Keep in mind what I said in this chapter’s introduction — training a custom Tesseract model is
**hard** work. The majority of the effort involves configuring your development environment.
Once your development environment is configured correctly, training your Tesseract model
becomes a breeze.

Tesseract is the world’s most popular open-source OCR engine. Someone else has likely
encountered the same error as you have. Copy and paste your error message in Google and
start reading GitHub Issues threads. It may take some time and patience, but you will
eventually find the solution.

Lastly, we will be downloading the English language and OSD Tesseract model files that
would otherwise be installed automatically if you were installing Tesseract using **apt-get**:
```bash
$ cd /usr/local/share/tessdata/  
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/eng.traineddata
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/osd.traineddata
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_tra.traineddata
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_tra_vert.traineddata
```
 

[Tesseract have three sets of .traineddata files on GitHub in three separate repositories. These are compatible with Tesseract 4.0x+ and 5.0.0.Alpha](https://tesseract-ocr.github.io/tessdoc/Data-Files.html).
|               | Trained models                                           | Speed                     | Accuracy                                  | Supports legacy | Retrainable |
|---------------|----------------------------------------------------------|---------------------------|-------------------------------------------|-----------------|-------------|
| [tessdata](https://github.com/tesseract-ocr/tessdata)      | Legacy + LSTM (integerized tessdata-best)                | Faster than tessdata-best | Slightly less accurate than tessdata-best | Yes             | No          |
| [tessdata-best](https://github.com/tesseract-ocr/tessdata_best) | LSTM only (based on langdata)                            | Slowest                   | Most accurate                             | No              | Yes         |
| [tessdata-fast](https://github.com/tesseract-ocr/tessdata_fast) | Integerized LSTM of a smaller network than tessdata-best | Fastest                   | Least accurate                            | No              | No          |

##### macOS
Installing Tesseract on macOS has a near identical set of commands as our Ubuntu install:
```bash
$ wget -O tesseract.zip https://github.com/tesseract-ocr/tesseract/archive/refs/tags/5.3.4.zip
$ unzip tesseract.zip
$ mv tesseract-5.3.4 tesseract
$ cd tesseract
$ ./autogen.sh
$ export PKG_CONFIG_PATH="/usr/local/opt/icu4c/lib/pkgconfig"
$ ./configure
$ make
$ sudo make install 
$ make training
$ sudo make training-install
```
The big difference here is that we need to explicitly set our PKG_CONFIG_PATH environment
variable to point to the **icu4c sym-link** we created in [Section macOS ](./README.md#macos) .

**⚠ Do not forget this export command — if you do, your Tesseract compile will error out.**

Lastly, we will be downloading the English language and OSD Tesseract model files that
would otherwise be installed automatically if you were installing Tesseract using brew:
```bash
$ cd /usr/local/share/tessdata/  
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/eng.traineddata
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/osd.traineddata
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_tra.traineddata
$ sudo wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_tra_vert.traineddata
```
 
### Step #3: Cloning tesstrain and Installing Requirements
At this point, you should have Tesseract v5.3.4, compiled from source, installed on your
system.
The next step is installing ``tesstrain``, a set of Python tools that allow us to work with ``make``
files to train custom Tesseract models.
Using ``tesstrain`` (https://github.com/tesseract-ocr/tesstrain#train), we can train and fine-tune Tesseract’s deep
learning-based LSTM models (the same model we’ve used to obtain high accuracy OCR
results throughout this text).
A detailed review of the LSTM architecture is outside the scope of this text, but if you need a
refresher, I recommend this fantastic intro tutorial by Christopher Olah (https://colah.github.io/posts/2015-08-Understanding-LSTMs/).

Perhaps most importantly, the ``tesstrain`` package provides instructions on how our training
dataset should be structured, making it far easier to build our dataset and train the model.

Let’s install the required Python packages required by ``tesstrain`` now:
```bash
$ cd ~
$ git clone https://github.com/tesseract-ocr/tesstrain
$ workon ocr
$ cd tesstrain
$ pip install -r requirements.txt
```
As you can see, installing tesstrain follows a basic setup.py install. All we have to do is
clone the repository, change directory, and install the packages.

I am using the ``workon`` command to access my ``ocr`` Python virtual environment, thus keeping
my Tesseract training Python libraries separate from my system Python packages.
> #### The command ``workon`` is belong Python virtual environment .
> ##### Install 
> ```bash
> $ pip3 install virtualenv virtualenvwrapper
> ```
> Add the environment variable ``~/.bashrc`` 
> ```bash
> #######################################################
> export WORKON_HOME=$HOME/.virtualenv_container
> # virtualenv env path
> 
> export VIRTUALENVWRAPPER_PYTHON=XXXX 
> # XXX is Python3 location path，use command -> "$ which python3"  to find it (/usr/bin/python3)
> 
> 
> source XXX 
> # XXX -> "$ which virtualenvwrapper.sh" to find the location path
> # ex: /home/someone/.local/bin/virtualenvwrapper.sh
> ####################################################### 
> ```
>  
> ##### Usage 
> ```bash
> $ mkvirtualenv <virtualenv NAME>
> # Create Virtualenv env
> # ex: mkvirtualenv tset1
> # ex: mkvirtualenv -p /usr/local/python36/bin/python3.6 tset2
> 
> $ cpvirtualenv <source virtualenv NAME> <new virtualenv NAME>
> # Copy Virtualenv env
> 
> $ rmvirtualenv <To remove virtualenv NAME>
> # Delete Virtualenv env
> 
> $ lsvirtualenv
> # Search Virtualenv env
> 
> $ workon <To load virtualenv NAME>
> # To use Virtualenv env
> # ex: workon test1 
> 
> $ deactivate
> # Escape Virtualenv env
> ```

Using Python virtual environments is the best practice and one I recommend you use. Still, if 
you want to install these packages into your system Python install, that’s okay as well (but
again, not recommended).

## Training Your Custom Tesseract Model
### Project Structure 
```bash
|-- training_data
|   |-- 01.gt.txt
|   |-- 01.png
|   |-- 02.gt.txt
|   |-- 02.png
...
|   |-- 18.gt.txt
|   |-- 18.png
|-- training_setup.sh
```
Our ``training_data`` directory is arguably the most important part of this project structure for
you to understand. Inside this directory, you’ll see that we have pairs of ``.txt`` and ``.png`` files.

The ``.png`` files are our images, containing the text in image format. The ``.txt`` files then have
the plaintext version of the text, such that a computer can read it from disk.

When training, Tesseract will load each ``.png`` image and ``.txt`` file, pass it through the LSTM,
and then update the model’s weights, ensuring that it makes better predictions during the next
batch.

**Most importantly, notice the naming conventions of the files in training_data.** For
each ``.png`` file, you also have a text file named ``XX.gt.txt``. For each image file, you must
have a text file with the same filename, but instead of a ``.png``, ``.jpg``, etc., extension, it must
have a ``.gt.txt`` extension. Tesseract can associate the images and ground-truth (``gt``) text
files together, but you must have the correct file names and extensions.

We’ll cover the actual dataset itself in the next section, but simply understand the naming
convention for the time being.

We then have a shell script, ``training_setup.sh``. This shell script handles setting an
important environment variable, ``TESSDATA_PREFIX``, which allows us to perform training and
inference.
### Tesseract Official Training Dataset 
To Read https://github.com/tesseract-ocr/tesstrain
```bash  
$ cd tesstrain 
$ unzip ocrd-testset.zip
```
### Our Tesseract Training Dataset
Ommitted...

### Creating Your Tesseract Training Dataset
You might be wondering why we are using Tesseract to train a custom handwriting recognition
model. Astute OCR practitioners will know that Tesseract doesn’t perform well on handwriting
recognition compared to typed text. *Why bother training a handwriting recognition model at
all?*

It boils down to three reasons:
1. **Readers ask all the time if it’s possible to train a Tesseract model for handwriting
recognition.** As you’ll see, it’s possible, and our custom model’s accuracy will be  ~10x
better than the default model, but it still leaves accuracy to be desired.
1. **Training a custom Tesseract model for typed text recognition is comparatively
“easy.”** Our goal in this chapter is to show you something you haven’t seen before.
3. **Most importantly, once you’ve trained a custom Tesseract model, you can train the
model on your data.** I suggest replicating the results of this chapter first to get a feel for
 the training process. From there, training your model is as easy as swapping the
``training_data`` directory for your images and ``.gt.txt`` files.

### Step #1: Setup the Base Model
Instead of training a Tesseract model from scratch, which is time-consuming, tedious, and
harder to do, we’re going to fine-tune an existing LSTM-based model.

The LSTM models included with Tesseract v4 are *much more accurate* than the non-deep
learning models in Tesseract v3, so I suggest you use these LSTM models and fine-tune them
rather than training from scratch.

Additionally, it’s worth mentioning here that Tesseract has three different types of model types:

1. **tessdata_fast**: These models balance speed vs. accuracy using integer-quantized
weights. These are also the default models that are included when you install Tesseract
on your machine.
2. **tessdata_best**: These models are the most accurate, using floating-point data types.
When fine-tuning a Tesseract model, you must start with these models.
3. **tessdata**: The old legacy OCR models from 2016. We will not need or utilize these
models.

You can learn more about each of these three model types in Tesseract’s documentation(https://tesseract-ocr.github.io/tessdoc/Data-Files.html).

You can use the following commands to change directory to  ``~/tesseract/tessdata`` and
then download the ``eng.traineddata`` file, which is the trained LSTM model for the English
language:
```bash
$ cd ~/tesseract
$ cd tessdata
$ wget https://raw.githubusercontent.com/tesseract-ocr/tessdata_best/main/eng.traineddata
```
Tesseract maintains a repository of all .traineddata model files for 124 languages here:
https://github.com/tesseract-ocr/tessdata_best

We use the English language model in this chapter. Still, you can just as easily replace the
English language model with a language of your choosing (provided there is a
``.traineddata`` model for that language, of course).

## Training Your Custom Tesseract Model

### Step #2: Set Your TESSDATA_PREFIX
With our ``.traineddata`` model downloaded (i.e., the weights of the model that we’ll be
fine-tuning), we now need to set an important environment variable ``TESSDATA_PREFIX``.

The ``TESSDATA_PREFIX`` variable needs to point to our ``tesseract/tessdata`` directory.

If you followed the install instructions (Section [Step #2: Building and Installing Tesseract Training Tools](./README.md#step-2-building-and-installing-tesseract-training-tools)), where we compiled Tesseract and its
training tools from scratch, then the ``tesseract/tessdata`` folder should be in your home
directory. Take a second now to verify the location of ``tesseract/tessdata`` —
double-check and triple-check this file path; setting the incorrect ``TESSDATA_PREFIX`` will
result in Tesseract being unable to find your training data and thus unable to train your model.

Inside the project directory structure for this chapter, you will find a file named ``training_setup.sh``. As the name suggests, this shell script sets your ``TESSDATA_PREFIX``.

Let’s open this file and inspect the contents now:
```bash
#!/bin/sh
export TESSDATA_PREFIX="/home/pyimagesearch/tesseract/tessdata"
```
Here you can see that I’ve supplied the *absolute path* to my ``tesseract/tessdata`` directory
on disk. You need to supply the absolute path; otherwise, the training command will error out.

Additionally, my username on this machine is ``pyimagesearch``. If you use the VM included
with your purchase of this text, this VM already has Tesseract and its training tools installed. If
your username is different, you will need to update the ``training_setup.sh`` file and replace the pyimagesearch text with your username.

To set the ``TESSDATA_PREFIX`` environment variable, you can run the following command:
```bash
$ source training_setup.sh
```

As a sanity check, let’s print the contents of the ``TESSDATA_PREFIX`` variable to our terminal:
```bash
$ echo $TESSDATA_PREFIX
/home/pyimagesearch/tesseract/tessdata
```

The final step is to verify the ``tesseract/tessdata`` directory exists on disk by copying and
pasting the above path into the ``ls`` command:
```bash
$ echo $TESSDATA_PREFIX
$ ls -l /home/pyimagesearch/tesseract/tessdata
total 15112
-rw-rw-r-- 1 ubuntu ubuntu 22456 Nov 24 08:29 Makefile
-rw-rw-r-- 1 ubuntu ubuntu 184 Dec 26 2019 Makefile.am
-rw-rw-r-- 1 ubuntu ubuntu 22008 Nov 24 08:29 Makefile.in
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov 24 08:29 configs
-rw-rw-r-- 1 ubuntu ubuntu 15400601 Nov 24 08:41 eng.traineddata
-rw-rw-r-- 1 ubuntu ubuntu 33 Dec 26 2019 eng.user-patterns
-rw-rw-r-- 1 ubuntu ubuntu 27 Dec 26 2019 eng.user-words
-rw-rw-r-- 1 ubuntu ubuntu 572 Dec 26 2019 pdf.ttf
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov 24 08:29 tessconfigs
```
If your output looks similar to mine, then you know your ``TESSDATA_PREFIX`` variable is set
correctly.

If your ``TESSDATA_PREFIX`` variable is set incorrectly, then ls will report an error:
```bash
$ ls -l /home/pyimagesearch/tesseract/tessdata
ls: /home/pyimagesearch/tesseract/tessdata: No such file or directory
```
This error implies that your path to ``tesseract/tessdata`` is incorrect. Go back and check
your file paths. **You need to have TESSDATA_PREFIX correctly set before continuing!**

### Step #3: Setup Your Training Data
In [Section Project Structure](./README.md#project-structure), we reviewed the directory structure and file organization Tesseract and
``tesstrain`` expect when training/fine-tuning a custom Tesseract OCR model. [Section Creating Your Tesseract Training Dataset](./README.md#creating-your-tesseract-training-dataset)
then provided suggestions on how to build your training dataset.

At this point, I’ll assume that you have your dataset properly organized on disk.

> For the sake of this example, I also suggest that you use the training data included in
> the directory structure of this project — walk before you run. Training a custom
> Tesseract model is hard, especially if this is your first time. I strongly encourage you to
> replicate our results before trying to train your models.

The following commands copy our training data from the ``training_data`` directory of this
project into ``tesstrain/handwriting-ground-truth``:
```bash
$ cd ~/tesstrain
$ mkdir data
$ cd data
$ mkdir handwriting-ground-truth
$ cd handwriting-ground-truth
$ cp -r ~/OCRPractitionerBundle_Code/chapter19-training_tesseract_model/training_data/*.* .
```
**The most important aspect of the above commands for you to understand is the naming convention.** Let’s break each of these commands down into components to
understand what we are doing:

First, a cd ``~/tesstrain`` changes the directory into our base ``tesstrain`` directory. We
then create a ``data`` directory and cd into it — we must create this ``data`` directory to store our
training data.

Inside the ``data`` directory, we then create a subdirectory named ``handwriting-groundtruth``.
You **must understand the naming convention of this directory**:

1. The ``handwriting`` portion of the subdirectory is *our model’s name* (which we’ll use in
our next section during training). You can name your model whatever you want, but I
suggest making it something specific to the project/task at hand, so you remember what
the intended use of the model is.
2. The second portion of the directory name, ``ground-truth``, tells Tesseract that this is
where our training data lives.

**When creating your training data directory structure, you must follow this naming
convention.**

After creating the **handwriting-ground-truth** directory and ``cd`` into it, we copy all of our
images and ``.txt`` files into it.

Once that is complete, we can train the actual model.


### Step #4: Fine-Tune the Tesseract Model
With our training data in place, we can now fine-tune our custom Tesseract model.
Open a terminal and execute the following commands:
```bash
$ workon ocr
$ cd ~/tesstrain
$ make training MODEL_NAME=handwriting START_MODEL=eng  TESSDATA=/home/pyimagesearch/tesseract/tessdata
```
First, I use the ``workon`` command to access the Python virtual environment where I have all
my ``tesstrain`` dependencies installed. As I mentioned earlier in this chapter, using a Python
virtual environment for these dependencies is *optional* but *suggested* (you should install the
packages in the system Python, for instance).

Next, we change directory into ``~/tesstrain``, where we have our Tesseract training utilities.

Training commences using the make command, the output of which you can see in
Figure 19.3. Here you can see the model training. Training will continue until the default
number of iterations, ``MAX_ITERATIONS=10000``, is reached.

On my machine, the entire training process took ~10 minutes. The training logs are shown in
Figure 19.4.  
After the training is completed, the final logs should look like Figure 19.4.  
But before we get too far, let’s break down the ``make`` command to ensure we understand each
of the parameters:
1. ``MODEL_NAME``: The name of the Tesseract model we are training. This value should be
the same as the directory you created in ``tesstrain/data``; that way, Tesseract knows
to associate the ``tesstrain/data/handwriting-ground-truth`` dataset with the
model we are training.
1. ``START_MODEL``: The name of the model we are fine-tuning. Recall that back in
[Section Step #1: Setup the Base Model](./README.md#step-1-setup-the-base-model), and we downloaded ``eng.traineddata`` to ``tesseract/tessdata`` —
that file holds the initial model weights that we will be fine-tuning.
1. ``TESSDATA``: The absolute path to our ``tesseract/tessdata`` directory where the
``handwriting`` subdirectory and training data are stored.

The previous three parameters are required to fine-tune the Tesseract model; however, it’s
worth noting that there are another two important hyperparameters that you may want to
consider fine-tuning:
1. ``MAX_ITERATIONS``: The total number of training iterations (similar to how Caffe iterations
default to ``10000``).
2. ``LEARNING_RATE``: The learning rate when fine-tuning our Tesseract model. This value
defaults to ``0.0001``. I recommend keeping the learning rate a relatively low value. If you
raise it too high, then the model’s pre-trained weights may be broken down too quickly
(i.e., before the model can take advantage of the pre-trained weights to learn patterns
specific to the current task).
3. ``PSM``: The default PSM mode to use when segmenting the characters from your training
images. You should use the ``tesseract`` command to test your example images with
varying PSM modes until you find the correct one for segmentation (see Chapter 11,
Improving OCR Results with Tesseract Options of the “Intro to OCR” Bundle for more
information on page segmentation modes).

I assume that as a deep learning practitioner, you understand the importance of fine-tuning
both your iterations and learning rate — fine-tuning these hyperparameters is crucial in
obtaining a higher accuracy OCR model.

A full list of hyperparameters available to you can be found on the GitHub repository for the
``tesstrain`` package (https://github.com/tesseract-ocr/tesstrain#train).

I’ll wrap up this chapter by saying if your training command errors out and you need to start
 again (e.g., you accidentally supplied the incorrect TESSDATA path), all you need do is run the
following command:
```bash
$ make clean MODEL_NAME=handwriting
```
Running ``make clean`` allows you to restart the training process. Make sure you specify the
MODEL_NAME. Otherwise, Tesseract will assume the default model name (which is foo).

**If you make training command errors out, I suggest you run ``make clean`` to clean up
and allow Tesseract a fresh start to train your model.**

### Training Tips and Suggestions
When training your custom Tesseract models, the first thing you need to do is set your
expectations. **For your first time around, it’s going to be hard, and the only way it will get
easier is to suffer through it, learning from your mistakes.**

There’s no “one easy trick.” There’s no shortcut. There’s no quick and dirty hack. Instead, you
need to put in the hours and the time.

**Secondly, accept that you’ll run into errors.** It’s inevitable. Don’t fight it, and don’t get
discouraged when it happens. You’ll miss/forget commands, and you may run into
development environment issues specific to your machine.

**When that happens, Google is your friend.** Tesseract is the world’s most popular OCR
engine. It’s more than likely that someone has encountered the same error as you have. Copy
and paste the error from your terminal, search for it on Google, and do your due diligence.

Yes, that is time-consuming. Yes, it’s a bit tedious. And yes, there will be more than one
false-start along the way.

Do you know what I have to say about that?

**Good. It means you’re learning.**

The notion that you can train a custom Tesseract model in your pajamas with a hot cup of tea
and someone massaging your shoulders, relaxing you into the process, is false. Accept that
it’s going to suck from time to time — if you can’t accept it, you won’t be able to learn how to
do it.

**Training a custom Tesseract model comes with experience. You have to earn it first.**

Finally, if you run into an error that no one else has documented online, post it on the
``tesstrain`` GitHub Issues page (https://github.com/tesseract-ocr/tesstrain/issues) so that the Tesseract developers can help you out. The Tesseract team is incredibly active and responds to bug reports and questions — utilize their knowledge to better yourself.

And above all, take your time and be patient. I know it can be frustrating. But you got this —
just one step at a time.

## Summary
In this chapter, you learned how to train and fine-tune a Tesseract OCR model on your custom
dataset.

As you learned, fine-tuning a Tesseract model on your dataset has very little to do with writing
code, and instead is all about:

1. Properly configuring your development environment
2. Installing the ``tesstrain`` package
3. Structuring your OCR training dataset in a manner Tesseract can understand
4. Setting the proper environment variables correctly
5. Running the correct training commands (and in the right order)

If you’ve ever worked with Caffe or the TensorFlow Object Detection API, then you know that
working with commands, rather than code, can be a catch-22:
* On the one hand, it’s easier since you aren’t writing code, and therefore don’t have to
worry about bugs, errors, logic issues, etc.
* But on the other hand, it’s **far harder** because you are left at the mercy of the Tesseract
training tools

**Instead, I suggest you remove the word “easy” from your vocabulary when training a
Tesseract model — it’s going to be hard — plain and simple.**

You need to adjust your mindset accordingly and walk in with an open mind, knowing that:
* The first (and probably the second and third) time you try to configure your development
environment for Tesseract, training will likely fail due to missed commands,
environment-specific error messages, etc.
* You’ll need to double-check and triple-check that your training data is stored correctly in
the ``tessdata`` directory
* Your training commands will error out if even the slightest configuration is correct
*  Additionally, the Tesseract training command will error out because you forgot to be in a
Python environment with the Python Imaging Library (PIL)/Pillow installed
* You’ll forget to run make clean when running the training command and then won’t be
able to get training to start again (and you may spend an hour or so banging your head
against the wall before you realize it)

**Accept that this is all part of the process**. It takes time and a lot of patience to get used to
training custom Tesseract models, but the more you do it, the easier it gets.

In the following chapter, we will take our trained custom Tesseract model and OCR an input
image.