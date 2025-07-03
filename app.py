import streamlit as st
import requests
import re

st.set_page_config("Daraz Price Tracker", "🛍️")
st.title("🛍️ Daraz Price Tracker (Bangladesh)")

url = st.text_input("🔗 Enter a Daraz product URL (daraz.com.bd):")

def extract_product_id(daraz_url):
    match = re.search(r"-p(\d+)", daraz_url)
    return match.group(1) if match else None

if url and "daraz.com.bd" not in url:
    st.warning("❌ Please enter a valid Daraz Bangladesh product URL")

if st.button("📊 Check Price") and url:
    product_id = extract_product_id(url)
    if product_id:
        api_url = f"https://api.daraz.com.bd/v2/product/{product_id}"
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            res = requests.get(api_url, headers=headers)
            if res.status_code == 200:
                data = res.json()
                name = data.get("data", {}).get("title", "Unnamed")
                price = data.get("data", {}).get("price", {}).get("discountPrice", "Unavailable")
                st.success(f"💰 Current Price of '{name}': ৳{price}")
            else:
                st.error("❌ Product not found or blocked.")
        except Exception as e:
            st.error(f"⚠️ Error fetching product: {e}")
    else:
        st.error("❌ Could not extract product ID from the URL.")

st.markdown("📌 Live price fetched from Daraz's mobile API.")
