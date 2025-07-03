import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config("Daraz Price Tracker", "🛍️")
st.title("🛍️ Daraz Price Tracker (Bangladesh)")

url = st.text_input("🔗 Enter a Daraz product URL:")

if url and "daraz.com.bd" not in url:
    st.warning("❌ This only works for URLs from daraz.com.bd")

if st.button("📊 Check Price") and url:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product title
        title_tag = soup.find("title")
        title = title_tag.get_text(strip=True).replace("| Daraz.com.bd", "") if title_tag else "Unnamed Product"

        # Extract price using known class or regex fallback
        price_tag = soup.find("span", string=re.compile(r"৳"))
        if not price_tag:
            price_tag = soup.find("div", string=re.compile(r"৳"))

        if price_tag:
            price_text = price_tag.get_text(strip=True)
            st.success(f"💰 Current Price for '{title}': {price_text}")
        else:
            st.error("⚠️ Price not found. Daraz may have updated their layout.")

    except Exception as e:
        st.error(f"⚠️ Failed to fetch product. Error: {e}")

st.markdown("""
---
📌 This tool fetches the current price of any Daraz product (Bangladesh). Bookmark the page and recheck daily!
""")
