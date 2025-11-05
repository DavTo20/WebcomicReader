# What it is

Webcomic reader is a lightweight and self-hosted webcomic server that you can access locally.
This does not include any webcomics but if you get your hands on the raw data of one preferably in a chapter format, this is the perfect tool to read them with.

# Features

- A lightweight webcomic reader
- Chapter select
- Saved progress in each chapter
- Sidebar
- Read chapters will be marked in the sidebar

# Disclaimer

This tool does not provide any copyrighted material. Preferably used by artists to test how their work flows from png to png. ]


# How to use

## Installation

Copy the repo
`git clone https://github.com/DavTo20/WebcomicReader`

To go to the directory inside the terminal
`cd ~/WebcomicReader` 

To run the server
`python3 -m https.server 8080` or any other port you'd like to use 

An all in one command to copy the Repo, open it, and then directly run the server.
```
git clone https://github.com/DavTo20/WebcomicReader
cd ~/WebcomicReader
mkdir webcomics
python3 -m http.server 8080
```

### Windows one liner setup

1. Install [Python 3](https://www.python.org/downloads/) and [Git](https://git-scm.com/download/win)
2. Open PowerShell and run:

```powershell
git clone https://github.com/DavTo20/WebcomicReader
cd WebcomicReader
mkdir webcomics
python -m http.server 8080
```

## Directory Structure

Inside `/WebcomicReader/` create a folder called `/webcomics/`, inside it you'll put your webcomics, they only work if they're inside their own directories and in already seperated into chapters

example:

WebcomicReader/<br/>
│<br/>
├── index.html<br/>
├── generateManifest.js<br/>
├── webcomics/<br/>
│   ├── Example1/<br/>
│   │   ├── Episode_001/<br/>
│   │   │   ├── 001.png<br/>
│   │   │   ├── 002.png<br/>
│   │   │   └── ...<br/>
│   │   ├── Episode_002/<br/>
│   │   │   ├── 001.png<br/>
│   │   │   └── ...<br/>
│   │   └── ...<br/>
│   ├── Example2/<br/>
│   │   ├── Episode_001/<br/>
│   │   ├── Episode_002/<br/>
│   │   └── ...<br/>
│   └── manifest.json<br/>
└── ...<br/>

### Once you moved your webcomics you'll need generate the manifest

To generate the manifest use 
```
cd ~/WebcomicReader
node generateManifest.js
```
## How to find your webcomic reader in the browser

In any browser type `localhost:8080` in the search tab once the server is running
