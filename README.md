![logo_shadowCL copie](https://github.com/natekali/ShadowCL/assets/117448792/1019b073-1b62-43fe-82d0-0d35d30ffbdd)
# ShadowCL
ShadowCL is the ultimate automated tool for crafting mail:password combolists effortlessly

## Features
* **Automated Combolist Generation**
* **Country-based Filtering & Worldwide/Mix**
* **Automated Notification and Cloud Upload**
* **Exclusion of Outlier Data from Wordlists**
* **Comprehensive Logging Functionality**

## Prerequisites
Before running ShadowCL, make sure you install these following libraries :
* tqdm
* requests

You can install them by typing this following command in your terminal :  
`pip3 install -r requirements.txt`

## Installation

Clone this repository to your local machine.

Open your terminal and navigate to the cloned repository.

Edit the `config/config.py` file with your [discord webhook url](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) and your [discord user id](https://www.businessinsider.com/guides/tech/discord-id?r=US&IR=T#:~:text=To%20find%20a%20user's%20Discord,sidebar%20and%20select%20Copy%20ID.).

Run the script by typing `python3 shadowCL.py` in your terminal.

Use the `-h` output to understand the necessary args.

Now, you can make your own configuration to generate your Combolist !

Upon completion of the script, a well-formatted Discord message will be delivered to you.

## Usage
**ShadowCL** can be used to create **authentic-looking** fake **combolists**, this tool is fully **automatic**, allowing you to run **multiple instances** simultaneously. The possibilities are **limitless**, you can **easily** generate combolists of **varying lengths** from **differents countries**, including **France**, **United-Kingdom**, **Poland**, **Russia**, **China**, and **USA**.

## Usage demo
Default usage : `python3 shadowCL.py`

<img width="615" alt="help" src="https://github.com/natekali/ShadowCL/assets/117448792/6d7ce046-62ad-4e6a-89ad-59e4aa06a103">

<br>
⠀
⠀

Generate a small combolist (100 entries) : `python3 shadowCL.py -l 100 -c mix -o demo.txt`

![demo](https://github.com/natekali/ShadowCL/assets/117448792/1446fd84-2ff8-41f5-a73b-e518daa8babf)

<br>

Multi-instances 100K combolists generation :
- `python3 shadowCL.py -1 100000 -o 100K_UHQ_COMBOLIST.txt`
- `python3 shadowCL.py -1 100000 -o 100K_UHQ_FR_COMBOLIST.txt -c fr`
- `python3 shadowCL.py -1 100000 -o 100K_UHQ_UK_COMBOLIST.txt -c uk`
- `python3 shadowCL.py -1 100000 -o 100K_UHQ_PL_COMBOLIST.txt -c pl`

![image](https://github.com/natekali/ShadowCL/assets/117448792/408fa61c-8f89-45d2-b506-38228aee37ef)

<br>

Discord webhook message example : 

<img width="702" alt="Capture d’écran 2024-02-05 à 19 58 48" src="https://github.com/natekali/ShadowCL/assets/117448792/1ab19c24-3c60-44fe-88ff-b18dead62015">

## Author
* [@natekali](https://github.com/natekali)

