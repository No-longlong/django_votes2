from django.shortcuts import render
from django.http import HttpResponse
import FinanceDataReader as fdr
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

def index(request):
    return HttpResponse("hello")

def  fdr(request):
    KOSPI = fdr.StockListing('KOSPI')
    return HttpResponse(KOSPI)