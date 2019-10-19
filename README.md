# first-gym-bot
Following [Siraj Raval's Youtube video](https://www.youtube.com/watch?v=3vxk91K1PiI&list=PL2-dafEMk2A7mfQDsEcmxxtxgFEZg0bW-)<br>
And learning gym for the first time in Oct 2019 and that too on windows 10 :)

Complete process to openAI gym on windows would be -
1. Download and extract [swigwin-4.0.1](http://www.swig.org/download.html)  (version may change later)
2. Add path of the extracted folder to windows environment.
3. Install Visual Studio Community with Microsoft Build Tools. Just google it.
4. `pip install Box2D`
5. `git clone https://github.com/openai/gym.git`<br>
   `cd gym`<br>
   `pip install -e .`
6. `git clone https://github.com/benelot/pybullet-gym.git`<br>
   `cd pybullet-gym`<br>
   `pip install -e .`


Issues with installing openai gym on windows-

If you do a full install of gym like shown in the video using -
`pip install gym[all]`
You are probably going to face problems since it failed for me.

<b>1. Box2D installation fails as swig not present. </b><br>
Box2D will not install properly since swig is not on your system. For that I referred to [answer](https://stackoverflow.com/a/54561280) by sliders_alpha.
He mentions it will not work for anaconda environments but I just restarted the terminal and it worked for me.
just do a-
`pip install Box2D`

but wait a minute--

<b>2. It also need Microsoft Build tools.</b><br>
Without it the Box2D installation still fails. So I installed Visual Studio Express 2019 with C++ and make sure u check
the Microsoft Build Tools 14 here. There maybe easier ways to do this but I did it this way and it worked.

Still openAI gym installation fails on windows...

<b>3. mujoco-py is needed for gym.</b><br>
Alternative is pybullets read [here](https://github.com/openai/gym)<br>
Go [here](https://github.com/benelot/pybullet-gym) to install pybullets instead and it works perfectly for me.
