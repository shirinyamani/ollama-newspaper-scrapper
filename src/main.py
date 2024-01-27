from api_utils import *
from scrape import *
import requests
import bs4
import openai
import os


if __name__ == "__main__":
    prompt = create_prompt()
    translate_and_summary(model='llama2', prompt=prompt, stream=False)