import streamlit as st
from daraz_scrapper import Daraz

st.set_page_config("Daraz Price Tracker", "🛍️")
st.title("🛍️ Daraz Price Tracker (BD)")

url = st.text_input("🔗 Enter a Daraz.com.bd product URL:")
if url and st.button("📊 Check Price"):
    try:
        dz = Daraz(url)
        data = dz.scrapeMe()
        if data and isinstance(data, list):
            product = data[0]
            title = product.get("name", "Unnamed")
            price = product.get("discount_price") or product.get("price", "Not found")
            st.success(f"💰 Current Price of **{title}**: {price}")
        else:
            st.error("⚠️ Failed to extract product details.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
st.markdown("""
---
📌 This tool fetches the current price of any Daraz product (Bangladesh). Bookmark the page and recheck daily!
""")
