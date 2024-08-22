This is a mini-project that would allow you to create your newsletter, sending out the latest news items from Hacker News (https://news.ycombinator.com/).
You can choose both the sender and receiver addresses.

## Environment
Upon cloning to your local git repo, create your own python virtual environment and download the dependencies:
`python3 -m venv [YOUR ENVIRONMENT NAME]
source [YOUR ENVIRONMENT NAME]/bin/activate
pip install -r ./requirements.txt`

### Environment Variables
Set these environment variables as you please:
`MY_EMAIL (the email address of the designated sender)
MY_PASSWORD (the password for the email address above)
MY_RECEIVING_EMAIL (the email address of the receiver)
LLAMA_API_TOKEN (the token for enabling the llama api - more details @ https://docs.llama-api.com/api-token)`
Please note that currently MY_EMAIL accepts only a gmail address. You can alter this by changing the smtp_server variable in main.py.

## Usage
In your virtual environment, run
`python3 main.py [POSITIVE_INT]`
where POSITIVE_INT can be any positive integer

## Output
The script would send a newsletter email from your MY_EMAIL address to your MY_RECEIVING_EMAIL address, containing a number of POSITIVE_INT stories. \
These stories are "top stories", meaning they have the most popularity of the day.\
There would also be a brief summary of each story summarized by the llama api, so that you can skim through the email and only pick the ones that interest you to read further.\
Templates for the email are stored under the directory "preview". 
\\
Enjoy! :D


