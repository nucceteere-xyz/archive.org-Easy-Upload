[<img alt="github" height="56" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/available/github_vector.svg">](https://github.com/nucceteere-xyz/archive.org-Easy-Upload)
[<img alt="git" height="56" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/available/git_vector.svg">](https://replit.com/@EngurRuzgar/Upload-to-Archiveorg)

## What is this?
This is a Python script for uploading files to archive.org
### How does it work?
It takes your credentials for archive.org and uploads the specified files through the IA library<br/>
## Usage
> [!CAUTION]
> We recomend using [Poetry](https://python-poetry.org/), if you dont have poetry, run these commands in your shell
> ```
> pip install internetarchive
> pip install python-dotenv
> ```
Run `git clone -b main https://github.com/nucceteere-xyz/archive.org-Easy-Upload.git`

After that, create a .env file in the working directory.<br/>
Inside of the .env file should look like this:
```.env
EMAIL=YOUR_ARCHIVE_ORG_EMAIL
PASSWD=YOUR_ARCHIVE_ORG_PASSWORD
ID=YOUR_ARCHIVE_ORG_ITEM_ID
```
After you do these, make sure that your env variables are set up correctly by running `env_check.py`.

