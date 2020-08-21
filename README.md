# Twitter sentiment
Simple twitter streamer & sentiment.

## How to run

To run; Just use steps below:

1. Install `python3`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/mohamadkhalaj/twitter_sentiment.git`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/mohamadkhalaj/twitter_sentiment.git && cd twitter_sentiment
  python3 -m venv venv  # Create virtualenv named venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
## How to use

1. First add keywords: python twitter_datamining.py apple OR python twitter_datamining.py apple samsung.
2. Wait to collect fresh tweets and then terminate app (if you don't, it collects all new tweets!).
3. After tweets collected run sentiment.py and see the results.
